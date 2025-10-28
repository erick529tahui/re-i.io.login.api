from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    lastName:str
    email: str
    password: str
    userId: str