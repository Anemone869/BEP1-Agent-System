from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"status": "后端服务启动成功啦！"}