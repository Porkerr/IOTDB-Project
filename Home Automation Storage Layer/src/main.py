from iotdb.Session import Session
from classes.Environment import *
from classes.Devices import *
from enums.DataType import DataType as dt
from enums.DeviceType import DeviceType as det
import string

import datetime

def main():
    # Database Setup
    
    ip = "127.0.0.1"
    port_ = "6667"
    username_ = "root"
    password_ = "root"
    session = Session(ip, port_, username_, password_)
    session.open(False)
    zone = session.get_time_zone()
    
    # Example environment & devices
    '''
    livingRoom = Environment(1, "livingroom", "Living Room", None)
    thermometer = Sensor(1, "thermometer", None, det.THERMOSTAT, "Nest", "Nest Learning Thermostat", dt.TEMPERATURE, 3.1)
    livingRoom.addDevice(thermometer)
    multimeter = Sensor(1, "multimeter", None, det.LIGHTING, "Brand", "Multimeter1", dt.VOLTAGE, 4)
    livingRoom.addDevice(multimeter)
    addEnvironmentToDatabase(livingRoom, session)
    '''

    # Manage the database (basic UI)
    userInputFlag = 1
    environmentList = list()
    environmentCount = 0
    deviceCount = 0

    '''
    # Create a dictionary that reflects the nodes in the database
    # keys = env
    while True:
        currentTime = datetime.datetime.now()
        value = random.randint(70, 110)
        session.insert_record(0, currentTime, {"root.kitchen.thermometer.temperature"}, {3}, {value})
        time.sleep(60.0)
    '''
    
    print("\nWelcome!")
    while userInputFlag:
        # Menu
        print("\nWhat would you like to do?")
        print("1. Add Environment")
        print("2. Add Device")
        # add timeseries
        #print("4. Show devices (testing)")
        #print("5. View data")
        #print("6. Database Overview")
        #print("9. Update database")
        print("0. Exit")


        # Interpret user choice
        choice = int(input())
        name = ""
        location = ""
        coordinates = None # PLACEHOLDER - null for now
        livingRoom = object

        if choice == 1: # add environment
            print("\nEnvironment name (lowercase, no spaces):")
            name = input()
            print("Location (e.g. Living Room):")
            location = input()
            print("Coordinates: (none for now)")
            coordinates = None          # PLACEHOLDER - null for now
            environmentList.append(Environment(environmentCount, name, location, coordinates))
            environmentCount += 1

            # don't need rn
            #print("Would you like to add any devices to it? (1 = no, 2 = yes)")
            #choice = int(input())

        if choice == 2: # add device
            # TODO - Read from environments in the system rather than ones created in the program
            # maybe save the list of environments in a file or something?
            
            print("\nChoose environment to add device to:")
            i = 0
            for env in environmentList:
                print(str(i) + ". " + env.name)
                i+=1
            envIndex = int(input())
            environmentAddTo = environmentList[envIndex]
            
            # Check if random or not
            print("Random or custom device (0 = random, 1 = custom)")
            deviceTypeChoice = int(input())
            if deviceTypeChoice == 0:

                randomSensor = Sensor(deviceCount).randomize()
                environmentAddTo.addDevice(randomSensor)
                deviceCount+=1
                
                addDeviceToDatabase(session, environmentAddTo.name, randomSensor.name, randomSensor.domain, 3) # 3 = float, all are float for now
                
                path = "root." + environmentAddTo.name + "." + randomSensor.name
                measurement = randomSensor.domain
                randomSensor.makeFakeDataInfinitely(path, measurement, 3, session)
                # TODO - run the randomly generated data thing
                
            else:
                print("What type of device (1 = Sensor, 2 = Actuator)")
                deviceChoice = int(input())

                print("Device name (lowercase, no spaces):")
                name = input()

                print("Coordinates: (none for now)")
                coordinates = None

                print("Domain:")
                print("1. THERMOSTAT")
                print("2. LIGHTING")
                print("3. HVAC")
                print("4. SECURITY")
                print("5. ENTERTAINMENT")
                print("6. APPLIANCE")
                domainChoice = int(input())
                
                domain = None
                domain_name = "none"
                match domainChoice:
                    case 1:
                        domain = det.THERMOSTAT
                        domain_name = "thermostat"
                    case 2:
                        domain = det.LIGHTING
                        domain_name = "lighting"
                    case 3:
                        domain = det.HVAC
                        domain_name = "HVAC"
                    case 4:
                        domain = det.SECURITY
                        domain_name = "SECURITY"
                    case 5:
                        domain = det.ENTERTAINMENT
                        domain_name = "entertainment"
                    case 6:
                        domain = det.APPLIANCE
                        domain_name = "appliance"

                print("Brand:")
                brand = input()

                print("Model:")
                model = input()

                print("Data Type:")
                print("1. TEMPERATURE")
                print("2. HUMIDITY")
                print("3. VOLTAGE")
                print("4. CURRENT")
                dataTypeChoice = int(input())
                dataTypeName = "none"

                match dataTypeChoice:
                    case 1:
                        dataType = dt.TEMPERATURE
                        dataTypeName = "temperature"
                    case 2:
                        dataType = dt.HUMIDITY
                        dataTypeName = "humidity"
                    case 3:
                        dataType = dt.VOLTAGE
                        dataTypeName = "voltage"
                    case 4:
                        dataType = dt.CURRENT
                        dataTypeName = "current"

                if deviceChoice == 1: # Sensor
                    Sensor1 = Sensor(deviceCount, name, coordinates, domainChoice, brand, model, dataType, 0)
                    environmentAddTo.addDevice(Sensor1)
                    
                    dev = addDeviceToDatabase(session, environmentAddTo.name, name, dataTypeName, 3)

                    path = "root." + environmentAddTo.name +"."+ name
                    Sensor1.makeFakeDataInfinitely(path, dataTypeName, 3, session)
                else: # Actuator
                    pass
                
                deviceCount += 1

                # Update the database!
                # DATA TYPE DEFAULTS TO FLOAT!!!!! Currently there aren't any non-float dataTypes.
                # moved::: dev = addDeviceToDatabase(session, environmentAddTo.name, name, dataTypeName, 3) # 3 = float
                
                # Make Fake Data
                #device_path = "root." + environmentName + "." + deviceName
                #makeFakeDataInfinitely(device_path, timeseriesNa  me, dataType, session)

        if choice == 4: # show devices
            #session.execute_query_statement("SHOW DEVICES")
            #print(session.count_measurements_in_template(""))

            pass
        
        elif choice == 5:
            pass
            # choose environment
                # choose device
                    # x - go back
                # go x - back

        elif choice == 0:
            # at the end of the loop (or may be after env / device adding) update the environment!
            userInputFlag = 0

    #TODO - add method to update database (add any non-added timeseries)

'''
Adds a device to the database.
    need: environment name -> device name -> what it's measuring + datatype
    dataType:
    - 0 = boolean
    - 1 = int32
    - 2 = int64
    - 3 = float
    - 4 = double
    - 5 = text (documentation says "text", i'm guessing this = string)
'''
def addDeviceToDatabase(session, environmentName: str, deviceName: str, timeseriesName: str, dataType: int):
    full_path = "root." + environmentName + "." + deviceName + "." + timeseriesName
    session.create_time_series(full_path, dataType, 0, 1, props=None, tags=None, attributes=None, alias=None) 

'''
Adds an entire environment to the database.
'''
def addEnvironmentToDatabase(environment, session):
    # If empty or device already in the database, exit
    if environment.deviceList.len() == 0:
        return
    
    # Get Environment Name
    environmentName = environment.name
    DATABASE_NAME = "root"
    pathPrefix = DATABASE_NAME + "." + environment.name 
    
    paths = []
    for device in environment.deviceList:
        keys = list(device.deviceState.keys())
        key = keys[0]    
        string = ""
        if key.value == 1:
            string = "temperature"
        elif key.value == 2:
            string = "humidity"
        elif key.value == 3:
            string = "voltage"
        elif key.value == 4:
            string = "current"
        path = pathPrefix + "." + device.name + "." + string
        dtype = type(device.deviceState[key])

        # add to path
        session.create_time_series(path, 4, 0, 1, props=None, tags=None, attributes=None, alias=None) #float filler for now
        paths.append(path)  
        print(dtype)

def updateDatabase():
    pass


main()






# To clear: visit each environment, delete timeseries root.<envname>.**


# Testing
#print(session.check_time_series_exists("root.environment.thermometer.status"))
#print(session.execute_query_statement("show databases"))
#session.delete_time_series(["root.environment.thermometer.*"])

#session.create_time_series("root.livingroom.thermometer.status0", 1, 0, 1, props=None, tags=None, attributes=None, alias=None)

