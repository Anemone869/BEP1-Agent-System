# BEP1-Agent-System

前后端分离的智能体对话系统。

## 项目结构

```
├── backend/
│   ├── main.py              # FastAPI 后端（/ping、/chat 接口）
│   ├── requirements.txt     # Python 依赖
│   ├── .env.example         # 环境变量模板
│   └── github_api_demo.py   # 第一周：调用 GitHub API 的演示脚本
├── frontend/
│   ├── index.html           # 前端聊天界面
│   └── README.md            # 前端运行说明
└── README.md
```

## 快速开始

### 1. 后端启动

```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 配置 API Key（首次运行前必须做）
cp .env.example .env
# 编辑 .env 文件，填入你的 API_KEY

# 启动服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. 前端使用

用浏览器打开 `frontend/index.html`，确保后端已启动在 `http://localhost:8000`。

### 3. 验证接口

- 浏览器访问 http://localhost:8000 → `{"hello":"world"}`
- 浏览器访问 http://localhost:8000/ping → `{"message":"pong"}`
- API 文档：http://localhost:8000/docs

### 4. 测试 /chat 接口

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "你好"}'
```

## 环境变量说明

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| API_KEY | 大模型 API 密钥 | 无（必须配置） |
| API_BASE_URL | API 地址 | https://api.siliconflow.cn/v1 |
| MODEL_NAME | 模型名称 | deepseek-ai/DeepSeek-V3 |

推荐使用[硅基流动](https://siliconflow.cn)注册获取 API Key（免费额度）。
