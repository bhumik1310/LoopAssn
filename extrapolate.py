import pytz
from dotenv import dotenv_values
from pymongo import MongoClient

from datetime import timezone,timedelta,datetime
config = dotenv_values(".env")

client = MongoClient("mongodb+srv://user:user@testdb.lz5fe4t.mongodb.net/?retryWrites=true&w=majority")
db = client["LoopDB"]
for x in client[config["DB_NAME"]]["rel-menu"].find():
    # Time_Zone = client[config["DB_NAME"]]["rel-timezones"].find_one({"store_id":x["store_id"]})
    # tmz = Time_Zone["timezone_str"]
    start = x["start_time"]
    end = x["end_time"]
    myset = set()
    for y in client[config["DB_NAME"]]['rel_times'].find({"store_id":x["store_id"]}):
        temp = y["timestamp_utc"][0:10]
        myset.add(temp)
        if "2023-01-19" not in myset: myset.add
        if "2023-01-20" not in myset:
            client[config["DB_NAME"]]["rel_times"].insert_one({"store_id":y["store_id"],"timestamp_utc":start,"status":"active"})
            client[config["DB_NAME"]]["rel_times"].insert_one(
                {"store_id": y["store_id"], "timestamp_utc": end, "status": "active"})
        if "2023-01-21" not in myset: myset.add("2023-01-21")
        if "2023-01-22" not in myset: myset.add("2023-01-22")
        if "2023-01-23" not in myset: myset.add("2023-01-23")
        if "2023-01-24" not in myset: myset.add("2023-01-20")
        if "2023-01-25" not in myset: myset.add("2023-01-20")

    print(sorted(myset))
