from typing import Optional
from fastapi import FastAPI
from pymongo import MongoClient
import pandas as pd

app = FastAPI()
client = MongoClient("mongodb+srv://dbAdmin:cmpt732@cluster732.jfbfw.mongodb.net")
db = client.KaggleProject
records = list(db["Income"].find())
print(type(records))
records = pd.DataFrame(records)





@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/mongo")
async def read_root():
    # return records
    return {"Hello": "World"}
    

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}