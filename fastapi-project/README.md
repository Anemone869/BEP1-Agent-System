# FastAPI 后端项目

## 项目简介
这是一个基于 FastAPI 的后端服务，提供基础接口和 `/chat` 大模型对话接口。

---

## 环境配置

### 1. 安装依赖
```bash
# 进入项目根目录
cd C:\Users\windows\Desktop\fastapi-project

# 安装所有依赖
pip install -r requirements.txt

### 2. 配置 API Key 环境变量
1. 复制项目中的 `.env.example` 文件，重命名为 `.env`
2. 打开 `.env` 文件，将 `your_api_key_here` 替换为你的真实大模型 API Key
3. 示例配置：
```env
API_KEY=你的真实API密钥
API_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-3.5-turbo

### 3. 启动后端服务
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000

### 4. 接口调用说明
- 接口文档地址：http://127.0.0.1:8000/docs
- 对话接口：`POST /chat`
- 请求示例：
```json
{
  "message": "你好"
}