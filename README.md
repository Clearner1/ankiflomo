# 📝 AnkiFlomo

一个类似 [Flomo](https://flomoapp.com/) 风格的 Anki 笔记管理器，通过 [AnkiConnect](https://foosoft.net/projects/anki-connect/) 插件连接你的 Anki，让你在浏览器中以更优雅的方式浏览、搜索和创建笔记。

![AnkiFlomo 截图](https://img.shields.io/badge/License-MIT-green?style=flat-square) ![AnkiConnect](https://img.shields.io/badge/AnkiConnect-v6-blue?style=flat-square)

## ✨ 功能特性

- 🏷️ **标签树** — 支持 `::` 层级结构，可折叠展开，点击按标签筛选笔记
- 📚 **牌组列表** — 展示所有牌组，点击按牌组筛选
- 📝 **笔记瀑布流** — 按时间倒序展示，无限滚动加载
- ✏️ **快速创建** — 选择牌组和模板，一键创建新笔记
- 🔍 **搜索** — 支持 Anki 原生搜索语法（如 `tag:Java`、`deck:Default`）
- 🟩 **复习热力图** — 可视化展示最近 16 周的复习记录
- 📊 **统计面板** — 笔记数、标签数、今日复习数
- 🔄 **同步** — 一键触发 Anki 同步
- 📱 **响应式** — 支持移动端自适应布局
- ⌨️ **快捷键** — `Ctrl/Cmd + K` 快速聚焦搜索框

## 📋 前置要求

1. **Anki** — 已安装 [Anki](https://apps.ankiweb.net/) 桌面版
2. **AnkiConnect 插件** — 在 Anki 中安装 AnkiConnect 插件（代码：`2055492159`）
   - 打开 Anki → 工具 → 插件 → 获取插件 → 输入 `2055492159` → 确定
   - 重启 Anki

## 🚀 快速开始

### 方法一：直接打开

```bash
# 克隆仓库
git clone https://github.com/Clearner1/ankiflomo.git
cd ankiflomo

# 直接用浏览器打开
open index.html        # macOS
xdg-open index.html    # Linux
start index.html       # Windows
```

### 方法二：本地服务器（推荐）

```bash
# 克隆仓库
git clone https://github.com/Clearner1/ankiflomo.git
cd ankiflomo

# 启动本地服务器
python3 -m http.server 3000

# 打开浏览器访问
# http://127.0.0.1:3000
```

> **⚠️ 注意：** 启动前请确保 Anki 已打开并且 AnkiConnect 插件已启用（默认监听 `127.0.0.1:8765`）。

## 🏗️ 项目结构

```
ankiflomo/
├── index.html    # 页面结构
├── style.css     # 样式（暗色侧边栏 + 亮色内容区）
├── app.js        # 应用逻辑（API 通信、标签树、笔记渲染）
└── README.md
```

## 🔧 技术栈

- **纯前端** — HTML + CSS + JavaScript，无需构建工具，无框架依赖
- **AnkiConnect API v6** — 通过 HTTP POST 请求与 Anki 通信
- **Google Fonts** — Inter + Noto Sans SC 字体

## 📖 使用说明

| 操作 | 说明 |
|------|------|
| 点击左侧标签 | 按标签筛选笔记 |
| 点击左侧牌组 | 按牌组筛选笔记 |
| 搜索框输入 | 支持 Anki 搜索语法，如 `tag:Java`、`deck:Default`、`added:1` |
| 顶部输入区 | 填写正面/背面内容，选择牌组和模板，点击保存创建笔记 |
| 笔记卡片上的标签 | 点击可快速按该标签筛选 |
| 🔄 同步按钮 | 触发 Anki 云同步 |
| `Cmd/Ctrl + K` | 快速聚焦搜索框 |

## 📄 License

MIT
