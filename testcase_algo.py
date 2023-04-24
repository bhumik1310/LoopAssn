import pytz
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


for y in client[config["DB_NAME"]]['testcase'].find():
     x = client[config["DB_NAME"]]['Menu_hours'].find_one({"store_id": y["store_id"]})
     tmz_cursor=client[config["DB_NAME"]]['TimeZone'].find_one({"store_id":y["store_id"]})
     tmz = tmz_cursor["timezone_str"]
     local_tmz = pytz.timezone(tmz)
     time_format = "%Y-%m-%d %H:%M:%S"

     start = y["timestamp_utc"][0:11] + x["start_time_local"]
     end = y["timestamp_utc"][0:11] + x["end_time_local"]
     naive_start = datetime.strptime(start,time_format)
     naive_end = datetime.strptime(end,time_format)
     local_start = local_tmz.localize(naive_start,is_dst=None)
     local_end = local_tmz.localize(naive_end, is_dst=None)
     utc_start = local_start.astimezone(pytz.utc)
     utc_end = local_end.astimezone(pytz.utc)


