# Environments

from classes.Devices import Device
import string
import numpy as np # for vectors

class Environment:
    # Add - make sure variables are a specific type
    id: int
    name: string
    location: string
    coordinates: np
    deviceList: list

    # Constructor - NEW METHOD (for testing)
    def __init__(self, id, name:string, location:string, coordinates:np):
        self.id = id
        self.name = name
        self.location = location
        self.coordinates = coordinates
        self.deviceList = list()

    # NEW METHOD
    def addDevice(self, device):
        self.deviceList.append(device)
