from fastapi import Body, FastAPI
from Models import UserModel

app = FastAPI(title="Login API",version="1.0.0")

@app.get("/health_check")
def read_root():
    return {"message":"API Health Check is OK"}


# **************** Login and Register *************************************


@app.post("/registerUser")
def register_user(userModel=Body(UserModel)):
    return {"User registered successfully"}

@app.post("/validateEmail")
def register_user(userModel=Body(UserModel)):
    return {"User registered successfully"}

@app.post("/passwordRecovery")
def register_user(userModel=Body(UserModel)):
    return {"Please rewiew your email to reset your password"}

@app.post("/generateToken")
def register_user(userModel=Body(UserModel)):
    return {"ASDD234234G565GHGHJJJKKKJJKK"}

@app.post("/renewToken")
def register_user(userModel=Body(UserModel)):
    return {"QWEREREER12321454545iuyuiyjK"}

@app.post("/getUserInformation")
def register_user(userModel=Body(UserModel)):
    return {"User found"}

@app.post("/login")
def register_user(userModel=Body(UserModel)):
    return {"login OK"}

@app.post("/logout")
def register_user(userModel=Body(UserModel)):
    return {"logout OK"}


# **************** Dashboard *************************************
