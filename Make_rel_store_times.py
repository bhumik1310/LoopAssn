import pytz

from pymongo import MongoClient

from datetime import timezone,timedelta,datetime


client = MongoClient("mongodb+srv://user:user@testdb.lz5fe4t.mongodb.net/?retryWrites=true&w=majority")
db = client["LoopDB"]

def create_tmz_object(date, time):
    time_format = "%Y-%m-%d %H:%M:%S"
    tmz_string = date + time
    naive_time = datetime.strptime(tmz_string, time_format)
    local_time = local_tmz.localize(naive_time, is_dst=None)
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time

for x in client["LoopDB"]['Menu_hours'].find({"day":2},no_cursor_timeout=True):
 print("running")
 for y in client["LoopDB"]['store_times'].find({"store_id":x["store_id"]},no_cursor_timeout=True):
      Time_Zone =  client["LoopDB"]['TimeZone'].find_one({"store_id":x["store_id"]},no_cursor_timeout=True)

      #Initialising Time-zone params

      tmz = Time_Zone["timezone_str"]
      local_tmz = pytz.timezone(tmz)

      #Creating time objects for comparison.

      utc_start = create_tmz_object(y["timestamp_utc"][0:11], x["start_time_local"])
      utc_end = create_tmz_object(y["timestamp_utc"][0:11], x["end_time_local"])
      utc_time = create_tmz_object(y["timestamp_utc"][0:11],y["timestamp_utc"][11:19])


      if utc_start < utc_time < utc_end:
          client["LoopDB"]['rel_times'].insert_one({"store_id": y["store_id"],
                                                             "status": y['status'], "timestamp_utc":y['timestamp_utc']})
