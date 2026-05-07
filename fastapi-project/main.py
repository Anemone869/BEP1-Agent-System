@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/ping")
def ping():
    return {"message":"pong"}
