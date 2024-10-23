# Contains all device classes
# 6/3/2024

import string
import random
import numpy as np # for vectors
from abc import ABC, abstractmethod
from enums.DeviceType import DeviceType
import time # NEW - for data gen
import datetime # NEW - for data gen
import os
import calendar
from iotdb.Session import Session
from classes.Environment import *
from classes.Devices import *

class Device(ABC):
    id: int
    name: string
    coordinates: np
    domain: DeviceType
    brand: string
    model: string
    deviceState: dict # = hash table

    # Constructor - NEW METHOD
    @abstractmethod
    def __init__(self):
        pass

    
class Display(Device): # Placeholder
    pass

class Sensor(Device):
    # Constructor - NEW METHOD
    def __init__(self, id = None, name = None, coordinates = None, domain = None, brand = None, model = None, dataType = None, data = None): # data = data being recorded
        if id == None and name == None and coordinates == None and domain == None and brand == None and model == None and dataType == None and data == None:
            self.id = id
            self.randomize()
        else:
            self.id = id
            self.name = name
            self.coordinates = coordinates
            self.domain = domain
            self.brand = brand
            self.model = model
            self.deviceState = {dataType: data} # CHANGE - maybe just change to the datatype & store data in the database
    '''
    def __init__(self, id): # NEW METHOD (only id, for randomizing)
        self.id = id
        self.randomize()
    '''
    def getSensorState(self):
        return self.deviceState
    def randomize(self):
        nameList = ["thermostat", "lighting", "HVAC", "security", "entertainment", "appliance"]
        coordinatesList = [None]
        domainList = ["temperature", "humidity", "voltage", "current"] # data type
        brandList = ["Nest", "HouseBrand", "Brand Name"]
        modelList = ["1400 thingthatworks", "Filler Model 1", "Filler Model 2"]
        
        self.name = random.choice(nameList)
        self.coordinates = random.choice(coordinatesList)
        self.domain = random.choice(domainList)
        self.brand = random.choice(brandList)
        self.model = random.choice(modelList)
        return self
    def makeFakeDataInfinitely(self, device_path, measurement, data_type, session): ## INCOMPLETE
        print("Enter the update rate in seconds: ")
        UPDATE_RATE = int(input())
        starttime = time.monotonic()
        
        #pid = os.fork()
        pid = 0
        if pid == 0: # if child
            while True:
                value = random.randint(70, 110)

                # Get time
                current_time = datetime.datetime.now(datetime.UTC) 
                current_time_epoch_sec = calendar.timegm(current_time.timetuple())
                current_time_epoch_ms = current_time_epoch_sec * 1000 # need to convert to ms :' server is in ms
                timestamp = current_time_epoch_ms

                '''
                # Generate fake data
                if data_type == 0: # bool
                    value = bool(random.getrandbits(1))
                elif data_type == 1 or data_type == 2:
                    value = random.randint(70, 110)
                elif data_type == 3 or data_type == 4:
                    value = random.uniform(70, 110)
                elif data_type == 3:
                    value = "randomized text"
                '''

                # Insert Record
                session.insert_record(device_path, timestamp, {measurement}, {data_type}, {value})
                
                # Pause
                time.sleep(UPDATE_RATE - ((time.monotonic() - starttime) % UPDATE_RATE))
        pass
        

class Actuator(Device): # Placeholder
    pass


