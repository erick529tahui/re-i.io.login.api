from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


@dataclass
class AudioFile:
    fileName:str
    filePath:str
    fileFormat:str
    MbSize:int
    duration:int

@dataclass
class Question:
    question:str
    answerText:str
    answerRecorded:AudioFile

#----------------------------------------------------------------

class ReIKnowledgeModel(BaseModel):

    def __init__(self,idKnowledge,description,percentage,start_date,end_date):
        self._idKnowledge = idKnowledge
        self._description = description
        self._percentage = percentage
        self._start_date = start_date
        self._end_date = end_date

    # _idKnowledge: int
    # _description: str
    # _percentage: int = Field(gt=0,lt=100)
    # _start_date: datetime
    # _end_date: datetime

    def get_description(self):
        return self._description
    


class LoadKnowledge(BaseModel):
    idKnowledge: int
    urls: List[str]=[]
    audios: List[AudioFile]=[]
    texts: List[str]=[]


class GuidedKnowledge(BaseModel):
    idKnowledge: int
    foda: List[Question]=[]
    porter: List[Question]=[]
    businessModelCanva: List[Question]=[]

#----------------------------------------------------------------


class CompletedAnalysisModel(BaseModel):
    idAnalysis: int
    description: str
    percentage: int = Field(gt=0,lt=100)
    start_date: datetime
    end_date: datetime
    

class RecomendationModel(BaseModel):
    idREcomendation: int
    description: str
    percentage: int = Field(gt=0,lt=100)
    start_date: datetime
    end_date: datetime


#----------------------------------------------------------------