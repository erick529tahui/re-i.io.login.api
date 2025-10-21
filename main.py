from fastapi import FastAPI

app = FastAPI(title="Login API",version="1.0.0")

@app.get("/health_check")
def read_root():
    return {"message":"API Health Check is OK"}

#@app.post("/register")
#def create_item(User: any):
#    return {"test register"}
