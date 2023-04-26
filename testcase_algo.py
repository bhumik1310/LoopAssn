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
def create_tmz_object(date,time):
     time_format = "%Y-%m-%d %H:%M:%S"
     tmz_string = date + time
     naive_time = datetime.strptime(tmz_string,time_format)
     local_time = local_tmz.localize(naive_time,is_dst=None)
     utc_time = local_time.astimezone(pytz.utc)
     return utc_time




for y in client[config["DB_NAME"]]['testcase'].find():                                      #function tests if testcase time is
                                                                                            # bw menu hours and
                                                                                            # adds it to a relevant database.
     x = client[config["DB_NAME"]]['Menu_hours'].find_one({"store_id": y["store_id"]})
     tmz_cursor=client[config["DB_NAME"]]['TimeZone'].find_one({"store_id":y["store_id"]})
     tmz = tmz_cursor["timezone_str"]
     local_tmz = pytz.timezone(tmz)




     utc_start= create_tmz_object(y["timestamp_utc"][0:11] , x["start_time_local"])
     utc_end = create_tmz_object(  y["timestamp_utc"][0:11] , x["end_time_local"])
     utc_time = create_tmz_object(y["timestamp_utc"][0:11],y["timestamp_utc"][11:19])

     if utc_start<utc_time<utc_end:
          client[config["DB_NAME"]]['rel_times'].insert_one({"store_id":y["store_id"],"status":y['status'],"timestamp_utc":
                                                             y['timestamp_utc']})
          print("time added....")


