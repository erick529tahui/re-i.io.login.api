from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    firstName: str
    lastName:str
    businessName:str
    website:str
    businessDoTxt: str
    businessDoRecord: bytes
    mainChanllengesTxt: str
    mainChanllengesRecord: bytes
    email: str
    hashed_password: str
    userId: str
    token: str
    expired_time: datetime