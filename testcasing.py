from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from datetime import timezone,timedelta,datetime
import string
import random
from threading import Timer
config = dotenv_values(".env")


client = MongoClient(config["MONGODB_CONNECTION_URI"])
db = client.config["DB_NAME"]
for x in client[config["DB_NAME"]]['Menu_hours'].find({"day":1}):
    for y in client[config["DB_NAME"]]['store_times'].find({'store_id': x['store_id']}):
        client[config["DB_NAME"]]['testcase'].insert_one({"store_id":y["store_id"],"status":y["status"],"timestamp_utc":y["timestamp_utc"]})
    break

