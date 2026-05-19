from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

app = FastAPI()

# 解决跨域问题（方便前端同学调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 读取环境变量
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

class ChatRequest(BaseModel):
    message: str

@app.get("/hello")
def hello():
    return {"message": "后端服务启动成功！"}

@app.post("/chat")
def chat(req: ChatRequest):
    if not API_KEY:
        return {"error": "请先配置API_KEY环境变量"}
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": req.message}]
    }
    
    try:
        resp = requests.post(f"{API_BASE_URL}/chat/completions", json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"error": str(e)}