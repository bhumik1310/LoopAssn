import pytz
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from datetime import timezone,timedelta,datetime
import string
import random
from threading import Timer
config = dotenv_values(".env")

from motor import motor_asyncio
from motor import motor_common
from motor import motor_gridfs



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

def get_data():

 Menu_hour_sheet = db["TimeZone"]

 y = client[config["DB_NAME"]]['Menu_hours'].find_one({'day':1})
 return y["store_id"]

# print(get_data())
def convert_timezone(x):
 for y in client[config["DB_NAME"]]['TimeZone'].find({"store_id":x["store_id"]}):
    tmz_info = y["timezone_str"]
    local_tmz = pytz.timezone(y["timezone_str"])
    time_str_start = + x["start_time_local"]
    time_str_end = x["end_time_local"]
    time_format = "%Y-%m-%d %H:%M:%S"
    naive_start_time = datetime.strptime(time_str_start,time_format)
    local_start_time = local_tmz.localize(naive_start_time,is_dst=None)
    utc_start_time=local_start_time.astimezone(pytz.utc)
    print(utc_start_time.strftime(time_format),x["start_time_local"] ,y["timezone_str"])
 #  print(x)
##TEST
for x in client[config["DB_NAME"]]['Menu_hours'].find():
 convert_timezone(x)
 # for y in client[config["DB_NAME"]]['store_times'].find({'store_id': x['store_id']}):
 #  time = y['timestamp_utc']
 #  print(time)

  # if y['timestamp_utc']<=x['end_time_local'] and y['timestamp_utc']>=x['start_time_local']:
  #  client[config["DB_NAME"]]["beacon"].insert_one({'store_id':y["store_id"],'time':y['timestamp_utc']})

# print(report_id)

##  Timezone conversion function ##

