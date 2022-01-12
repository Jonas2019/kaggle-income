from pymongo import MongoClient
import pandas as pd
from bson.objectid import ObjectId


# mongoURI = "[Enter URI Here]"
mongoURI = "mongodb+srv://dbAdmin:cmpt732@cluster732.jfbfw.mongodb.net"
client = MongoClient(mongoURI)
db = client.KaggleProject

records = list(db["Income"].find())
print(type(records))
# records = pd.DataFrame(records)

def incomeMapper(income) -> dict:
    return {
        "id": str(income["_id"]),
    "workclass": str(income["workclass"]),
    "fnlwgt": str(income["fnlwgt"]),
    "education":str(income["education"]),
    "educational": str(income["educational-num"]),
    "marital": str(income["marital-status"]),
    "occupation": str(income["occupation"]),
    "relationship": str(income["relationship"]),
    "race": str(income["race"]),
    "gender": str(income["gender"]),
    "capitalGain": str(income["capital-gain"]),
    "capitalLoss": str(income["capital-loss"]),
    "hoursPerWeek": str(income["hours-per-week"]),
    "nativeCountry": str(income["native-country"]),
    "fiftyK": str(income["income_>50K"])
    }


# Retrieve all students present in the database
async def retrieve_incomes():
    # print(db["Income"].find())
    incomes = []
    async for income in db["Income"].find():
        incomes.append(incomeMapper(income))
    return incomes