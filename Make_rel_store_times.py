import pytz
from pymongo import MongoClient

from datetime import timezone,timedelta,datetime

##Creating a relevant_times collection which only contains store-times in between the menu-hours and discards all the redundant data.
## Day two has been hardcoded as start and end times for each day are assumed to be same. Cuts search by a factor of 6.

##Also looks at the dates to see which ones in the current week are missing and adds start/end times of those dates as data points
##in rel_times assuming that the store was open throughout the Menu_Hours. The for loop for this condition doesn't work because
## the string comparator doesn't seem to equalise typecasted strings with normal ones.


#Should be ideally run centrally , sifts through the dynamic csv's to maintain a list free of irrelevant datatimes(which do not lie in
#the menu hours , but still exist in store_times , and is redundant to run these operations everytime a report has to be generated.
#A trigger can be bound to the end of the collection cursors to identify a modification in the store-time csv to rerun a part of this
#to essentially sort the new element.

client = MongoClient("mongodb+srv://user:user@testdb.lz5fe4t.mongodb.net/?retryWrites=true&w=majority")
db = client["LoopDB"]

def create_tmz_object(date, time):
    time_format = "%Y-%m-%d %H:%M:%S"
    tmz_string = date + time
    naive_time = datetime.strptime(tmz_string, time_format)
    local_time = local_tmz.localize(naive_time, is_dst=None)
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time

#Any day can be chosen to fetch the menu hours for the current example , however uncomment this code and replace if each day has
# different menu-hours timings.
# for i in range(6):
#     for x in client["LoopDB"]['Menu_hours'].find({"day": i}):


for x in client["LoopDB"]['Menu_hours'].find({"day":2}):
 Time_Zone = client["LoopDB"]['TimeZone'].find_one({"store_id": x["store_id"]})
 tmz = Time_Zone["timezone_str"]
 client["LoopDB"]['rel-menu'].insert_one({"store_id": x["store_id"], "start_time":x["start_time_local"],"end_time":x["end_time_local"]})
 client["LoopDB"]['rel_timezones'].insert_one({"store_id": x["store_id"], "timezone_str": tmz})

 #Uncomment this print prompt if debugging this function to see where this code fails , mostly mongo gives an error when cursor
 #instances expire after 30 mins of usage, so if the failing cursor is known , the cursor time can be reset and the code will
 #keep on working.
 # print("running")


 utc_end=0
 utc_start=0

 myset = set()

 for y in client["LoopDB"]['store_times'].find({"store_id":x["store_id"]}):

      #Initialising Time-zone params


      local_tmz = pytz.timezone(tmz)
      utc_tmz = pytz.timezone("UTC")
      time_format = "%Y-%m-%d %H:%M:%S"
      tmz_string =y["timestamp_utc"][0:11] + y["timestamp_utc"][11:19]
      naive_time = datetime.strptime(tmz_string, time_format)
      local_time = utc_tmz.localize(naive_time, is_dst=None)
      utc_time = local_time.astimezone(pytz.utc)

      #Creating time objects for comparison.

      utc_start = create_tmz_object(y["timestamp_utc"][0:11], x["start_time_local"])
      utc_end = create_tmz_object(y["timestamp_utc"][0:11], x["end_time_local"])
      # utc_time = create_tmz_object(y["timestamp_utc"][0:11],y["timestamp_utc"][11:19])





      #If the time is relevant i.e lies in the menu hours for that day , this snippet runs
      if utc_start < utc_time < utc_end:
          client["LoopDB"]['rel_times'].insert_one({"store_id": y["store_id"],
                                                             "status": y['status'], "timestamp_utc":y['timestamp_utc']})
          temp = datetime.strftime(utc_time,"%Y-%m-%d %H:%M:%S")

          myset.add(temp[0:10])

 if "2023-01-19" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-19" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-19" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-20" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-20" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-20" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-21" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-21" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-21" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-22" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-22" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-22" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-23" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-23" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-23" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-24" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-24" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-24" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

 if "2023-01-25" not in myset:
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-25" + " " + datetime.strftime(utc_start,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})
     client["LoopDB"]['rel_times'].insert_one({"store_id": x["store_id"],
                                               "status": "active",
                                               "timestamp_utc": "2023-01-25" + " " + datetime.strftime(utc_end,
                                                                                                       "%Y-%m-%d %H:%M:%S")[
                                                                                     11:] + " UTC"})

