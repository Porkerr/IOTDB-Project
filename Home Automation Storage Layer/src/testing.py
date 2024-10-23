# Server Stuff
from iotdb.Session import Session
from classes.Environment import *
from classes.Devices import *

# More things :3
import random
import datetime
import time
import calendar

# Server Setup
ip = "127.0.0.1"
port_ = "6667"
username_ = "root"
password_ = "root"
session = Session(ip, port_, username_, password_)
session.open(False)
zone = session.get_time_zone()

#
# Testing Zone >;333
#

# Main code! Don't delete >:
'''
# Get the current time
current_time = datetime.datetime.now(datetime.UTC) 
current_time_epoch_sec = calendar.timegm(current_time.timetuple())
current_time_epoch_ms = current_time_epoch_sec * 1000 # need to convert to ms :' server is in ms
TIMESTAMP = current_time_epoch_ms

# Generate value
value = random.randint(70, 110)

# Choose device
ID = "root.kitchen.thermometer" # aka device 
MEASUREMENTS = {"temperature"}

session.insert_record(ID, TIMESTAMP, MEASUREMENTS, {3}, {value})
print("insertion sent!")
'''
# Update Loop
print("Enter the update rate in seconds: ")
UPDATE_RATE = int(input())# how often data is sent to the server
starttime = time.monotonic()

while True:
    # Get time
    current_time = datetime.datetime.now(datetime.UTC) 
    current_time_epoch_sec = calendar.timegm(current_time.timetuple())
    current_time_epoch_ms = current_time_epoch_sec * 1000 # need to convert to ms :' server is in ms
    TIMESTAMP = current_time_epoch_ms

    # Generate fake data
    value_1 = random.randint(70, 110)
    value_2 = random.randint(70, 110)
    value_3 = random.randint(70, 110)
    value_4 = random.randint(70, 110)

    # Choose devices
    ID_1 = "root.kitchen.thermometer" # aka device 
    MEASUREMENTS_1 = {"temperature"}
    ID_2 = "root.kitchen.entertainment" # aka device 
    MEASUREMENTS_2 = {"brightness"}
    ID_3 = "root.kitchen.oven" # aka device 
    MEASUREMENTS_3 = {"temperature"}
    ID_4 = "root.kitchen.dishwasher" # aka device 
    MEASUREMENTS_4 = {"power_consumption"}
    

    session.insert_record(ID_1, TIMESTAMP, MEASUREMENTS_1, {3}, {value_1})
    session.insert_record(ID_2, TIMESTAMP, MEASUREMENTS_2, {3}, {value_2})
    session.insert_record(ID_3, TIMESTAMP, MEASUREMENTS_3, {3}, {value_3})
    session.insert_record(ID_4, TIMESTAMP, MEASUREMENTS_4, {3}, {value_4})
    print("insertions sent!")
    
    # Pause between data updates
    time.sleep(UPDATE_RATE - ((time.monotonic() - starttime) % UPDATE_RATE))


'''
from enums.DataType import DataType

data = DataType.TEMPERATURE

print(data.value)

print("Hello world!")




# IoTDB
def buildPath(environmentName, deviceName):
    pass

session.create_time_series(ts_path, data_type, encoding, compressor,
    props=None, tags=None, attributes=None, alias=None)
      
session.create_multi_time_series(
    ts_path_lst, data_type_lst, encoding_lst, compressor_lst,
    props_lst=None, tags_lst=None, attributes_lst=None, alias_lst=None
)
'''