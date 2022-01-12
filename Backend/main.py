from fastapi import FastAPI
from database import retrieve_incomes
from routes.income import router as IncomeRouter
from models.incomeRecords import (
    ErrorResponseModel,
    ResponseModel,
    IncomeSchema,
    UpdateIncomeModel,
)



app = FastAPI()
app.include_router(IncomeRouter, tags=["Income"], prefix="/income")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}