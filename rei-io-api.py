import os
from fastapi import Body, FastAPI
from Models import UserModel, LoginModel, RegisterUserModel , Token
from dotenv import load_dotenv
from datetime import datetime
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

#from typing import optional


#CHECK if this will be necessary
import secrets
AUTO_GENERATE_SECRET_KEY = secrets.token_urlsafe(32)


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY",AUTO_GENERATE_SECRET_KEY)
ALGORITHM = os.getenv("ALGORITHM","HS256")
ACCES_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCES_TOKEN_EXPIRE_MINUTES","30"))


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

security = HTTPBearer()



app = FastAPI(title="Rei-io Login API",version="1.0.0")



# **************** Login and Register *************************************

@app.get("/healthCheck")
def health_check():
    return {"message":"API Health Check is OK"}



@app.post("/registerUser")
def register_user(registerModel=Body(RegisterUserModel)):
    return {"User registered successfully"}

@app.post("/login")
def login_user(loginRequest=Body(LoginModel)):
    return {"login OK"}

@app.post("/logout")
def logout_user(userModel=Body(UserModel)):
    return {"logout OK"}

@app.post("/generateToken")
def generate_token(userModel=Body(UserModel)):
    return {"ASDD234234G565GHGHJJJKKKJJKK"}

@app.post("/renewToken")
def renew_token(userModel=Body(UserModel)):
    return {"QWEREREER12321454545iuyuiyjK"}

@app.post("/validateEmail")
def validate_email(userModel=Body(UserModel)):
    return {"User registered successfully"}

@app.post("/passwordRecovery")
def password_recovery(userModel=Body(UserModel)):
    return {"Please rewiew your email to reset your password"}



@app.post("/getUserInformation")
def get_user_information(userModel=Body(UserModel)):
    return {"User found"}


# **************** Dashboard *************************************
