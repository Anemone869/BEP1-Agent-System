from fastapi import FastAPI#1.1创建fastapi环境
from fastapi .middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app=FastAPI()#2.5允许前端跨域访问

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)#2前端网页调用接口时的必需品(仅后端测试时可删)

client=OpenAI(
    api_key="opkey",
    base_url="http://localhost:11434/v1"
)#opkey为自定义字符串
#Ollama本地模型的固定地址

def ask_llm(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="qwen:0.5b",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"出错了：{str(e)}"#本地模型

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/ping")
def ping():
    return {"message":"pong"} 

class ChatRequest(BaseModel):
    question:str
@app.post("/chat")#2.1新增post接口chat
def chat(request:ChatRequest):
    user_question=request.question#JSON接入用户问题
    ai_answer=ask_llm(user_question)#调用ask_llm函数
    return {"answer":ai_answer}#返回ai的回复结果
