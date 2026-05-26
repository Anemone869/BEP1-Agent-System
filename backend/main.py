import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.siliconflow.cn/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-ai/DeepSeek-V3")


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


def ask_llm(question: str) -> str:
    if not API_KEY:
        return "错误：请先配置 API_KEY 环境变量（复制 .env.example 为 .env 并填入真实密钥）"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": question}],
    }

    try:
        resp = requests.post(
            f"{API_BASE_URL}/chat/completions",
            json=payload,
            headers=headers,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.Timeout:
        return "请求超时，请稍后重试"
    except requests.exceptions.ConnectionError:
        return "无法连接到大模型服务，请检查 API_BASE_URL 是否正确"
    except Exception as e:
        return f"调用大模型出错：{str(e)}"


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):
    user_question = request.question
    ai_answer = ask_llm(user_question)
    return {"answer": ai_answer}
