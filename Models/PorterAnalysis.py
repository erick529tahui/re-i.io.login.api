from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


@dataclass
class Force:
    idForce:int
    bulletPoints:List[str]
    

class PorterAnalysisModel(BaseModel):
    idPorterAnalysis: int
    description: str
    estimated_time: str
    percentage: int = Field(gt=0,lt=100)
    start_date: datetime
    end_date: datetime


class PorterResultsModel(BaseModel):
    idPorterAnalysis: int
    header:str
    description: str
    forceList:List[Force]
    strategic_summary: str
    