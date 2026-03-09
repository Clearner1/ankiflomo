"""
Ankimo 本地开发服务器
- 静态文件服务（替代 python -m http.server）
- /api/tts 代理 MiniMax TTS API（解决 CORS）
"""
import http.server
import json
import urllib.request
import urllib.error

PORT = 3000
TTS_API = "https://api.minimaxi.com/v1/t2a_v2"


class AnkimoHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/tts":
            self._proxy_tts()
        else:
            self.send_error(404)

    def _proxy_tts(self):
        try:
            content_len = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_len)
            api_key = self.headers.get("X-API-Key", "")

            req = urllib.request.Request(
                TTS_API,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
                method="POST",
            )

            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data)

        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(error_body.encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-API-Key")
        self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), AnkimoHandler) as httpd:
        print(f"🚀 Ankimo server running at http://127.0.0.1:{PORT}")
        print(f"   Static files: current directory")
        print(f"   TTS proxy:    POST /api/tts -> {TTS_API}")
        httpd.serve_forever()
