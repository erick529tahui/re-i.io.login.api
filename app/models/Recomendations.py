from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field



@dataclass
class ActionPlan:
    idActionPlan:int
    idRol:int
    rol_name: str
    bulletPlanList: List[str]= []
    time_line: str
    budget: str
    kpis: List[str]= []


@dataclass
class Recomendation:
    idRecomendation:int
    description: str
    actionPlanList:List[ List[ActionPlan]] = []



class BusinessChallengeModel(BaseModel):
    idChallenge: int
    challenge_header: str
    challenge_description: str
    challenge_type: str
    recomendationList:List[Recomendation]= []

