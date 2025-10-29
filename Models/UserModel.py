from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    name: str
    lastName:str
    email: str
    hashed_password: str
    userId: str
    token: str
    expired_time: datetime