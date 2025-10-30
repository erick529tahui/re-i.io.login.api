from pydantic import BaseModel
from datetime import datetime

class UserModel(BaseModel):
    firstName: str
    lastName:str
    businessName:str
    website:str
    businessDoTxt: str
    businessDoRecord: bytearray[1024]
    mainChanllengesTxt: str
    mainChanllengesRecord: bytearray[1024]
    email: str
    hashed_password: str
    userId: str
    token: str
    expired_time: datetime