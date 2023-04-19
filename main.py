from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
import string
import random
from threading import Timer
config = dotenv_values(".env")

from motor import motor_asyncio
from motor import motor_common
from motor import motor_gridfs



app = FastAPI()

report_id
client = MongoClient(config["MONGODB_CONNECTION_URI"])
db = client.config["DB_NAME"]

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

## Generating a random report id
@app.get("/trigger_report")
async def get_report_id():
 N=10
 res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
 report_id =str(res)
 client[config["DB_NAME"]]["report_Ids"].insert_one({'report_id':report_id})
 return {"Report-ID":f"{report_id}"}
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]




@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

def get_data():
 client = MongoClient(config["MONGODB_CONNECTION_URI"])
 db = client.config["DB_NAME"]
 Menu_hour_sheet = db["TimeZone"]

 y = client[config["DB_NAME"]]['TimeZone'].find_one({'timezone_str':'Asia/Beirut'})
 return y

print(get_data())
print(report_id)

# @app.get("/trigger_report")
# async def returnId(id: int):
#     return {}:
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["mongodb+srv://user:user@testdb.lz5fe4t.mongodb.net/TestDB"])
# db = client.LoopDB
# for item in db.collection1.find():
#     _id = item['_id']
#     item2 = db.collection2.find({'_id':_id})
#     print "{}: {}, {}: {}, diff: {}, a>b?:{}".format(
#         item['name'], item['price'], item1['name'],
#         item1['price'], item['price'] - item1['price'],
#         item['price'] > item1['price'])
