from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    retrieve_incomes
)
from models.incomeRecords import (
    ErrorResponseModel,
    ResponseModel,
    IncomeSchema,
    UpdateIncomeModel,
)
router = APIRouter()

@router.get("/", response_description="Income records retrieved")
async def get_students():
    incomes = await retrieve_incomes()
    if incomes:
        return ResponseModel(incomes, "incomes data retrieved successfully")
    return ResponseModel(incomes, "Empty list returned")
