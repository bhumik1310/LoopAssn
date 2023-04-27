import pytz
import pymongo
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from datetime import timezone,timedelta,datetime
import string
import random
from threading import Timer
config = dotenv_values(".env")




app = FastAPI()


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



@app.get("/generate_new_report")              #Fetches the most recent report Id generated and will use this ID for returning the CSV
async def hello_program():
    report = client[config["DB_NAME"]]['report_Ids'].find_one(
        {},
        sort=[('_id', pymongo.DESCENDING)]
    )
    report_id = report["report_id"]
    return {"Report-ID": f"{report_id}"}













