from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class IncomeSchema(BaseModel):
    age: str = Field(...)
    workclass: str = Field(...)
    fnlwgt: str = Field(...)
    education: str = Field(...)
    educational: str = Field(...)
    marital: str = Field(...)
    occupation: str = Field(...)
    relationship: str = Field(...)
    race: str = Field(...)
    gender: str = Field(...)
    capitalGain: str = Field(...)
    capitalLoss: str = Field(...)
    hoursPerWeek: str = Field(...)
    nativeCountry: str = Field(...)
    fiftyK: str = Field(...)


class UpdateIncomeModel(BaseModel):
    age: Optional[str]
    workclass: Optional[str]
    fnlwgt: Optional[str]
    education: Optional[str]
    educational: Optional[str]
    marital: Optional[str]
    occupation: Optional[str]
    relationship: Optional[str]
    race: Optional[str]
    gender: Optional[str]
    capitalGain: Optional[str]
    capitalLoss: Optional[str]
    hoursPerWeek: Optional[str]
    nativeCountry: Optional[str]
    fiftyK: Optional[str]

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}