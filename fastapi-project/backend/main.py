import requests
import json

# 1. 函数：获取 GitHub API 信息（GET）
def get_github_info():
    url = "https://api.github.com/repos/python/cpython"
    print(f"\n🔍 正在请求: {url}")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # 将返回的 JSON 转为字典
        return data
    else:
        print(f"请求失败，状态码: {response.status_code}")
        return None

# 2. 函数：发送 POST 请求到 httpbin
def send_post_request():
    url = "https://httpbin.org/post"
    
    # 使用字典构造要发送的数据
    post_data = {
        "name": "王晨宁",
        "task": "Python模块学习",
        "language": "Python",
        "framework": "requests"
    }
    
    # 使用列表展示多个请求头
    headers_list = [
        "Content-Type: application/json",
        "User-Agent: PythonLearningScript"
    ]
    # 将列表转为字典（requests 需要字典格式）
    headers = {item.split(": ")[0]: item.split(": ")[1] for item in headers_list}
    
    print(f"\n📤 正在发送 POST 请求到: {url}")
    response = requests.post(url, json=post_data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"POST 请求失败，状态码: {response.status_code}")
        return None

# 3. 主函数：运行脚本并打印结果
def main():
    print("=" * 50)
    print("Python 模块学习 - API 调用示例")
    print("=" * 50)
    
    # 任务1：获取 GitHub 信息
    github_data = get_github_info()
    
    if github_data:
        print("\n✅ GitHub API 返回数据（部分展示）:")
        # 展示字典中的几个键值
        print(f"   - 仓库名: {github_data.get('full_name')}")
        print(f"   - 描述: {github_data.get('description', '无')[:80]}...")
        print(f"   - Stars: {github_data.get('stargazers_count')}")
        print(f"   - 语言: {github_data.get('language')}")
        print(f"   - 克隆地址: {github_data.get('clone_url')}")
    
    # 任务2：发送 POST 请求
    post_result = send_post_request()
    
    if post_result:
        print("\n✅ POST 请求返回数据:")
        # 打印完整的 JSON（格式化）
        print(json.dumps(post_result, indent=2, ensure_ascii=False))
        
        # 额外展示从返回数据中提取的信息
        print("\n📌 从 POST 响应中提取的信息:")
        print(f"   - 你发送的 json 数据: {post_result.get('json')}")
        print(f"   - 请求头中的 User-Agent: {post_result.get('headers', {}).get('User-Agent')}")

if __name__ == "__main__":
    main()from fastapi import FastAPI#1.1创建fastapi环境
from fastapi .middleware.cors import CORSMiddleware
from pydantic import BaseModel

app=FastAPI()#2.5允许前端跨域访问

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)#2前端网页调用接口时的必需品(仅后端测试时可删)

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/ping")
def ping():
    return {"message":"pong"}

def ask_llm(question:str)->str:
    return f"回答:{question}"#利用ai来回复用户问题

class ChatRequest(BaseModel):
    question:str
@app.post("/chat")#2.1新增post接口chat
def chat(request:ChatRequest):
    user_question=request.question#JSON接入用户问题
    ai_answer=ask_llm(user_question)#调用ask_llm函数
    return {"answer":ai_answer}#返回ai的回复结果
