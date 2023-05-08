import configparser
defaultConfigFile = "RobotToolsConfig.ini" # do not change unless you also change in main.py

def genConfigFile():
    config = configparser.ConfigParser()
    config.add_section("defaultValues")
    
    config.set("defaultValues", "defaultLogFile", "logFile.txt")
    config.set("defaultValues", "defaultDataFile", "dataFile.txt")
    config.set("defaultValues", "defaultLogMessageType", "INFO")
    config.set("defaultValues", "defaultTimerLogMessageType", "TIMER")
    config.set("defaultValues", "defaultTimerMessage", "default timer")
    config.set("defaultValues", "DebugToggle", "True")
    config.set("defaultValues", "LogSettings", "True")
    config.set("defaultValues", "ClearLogFile", "True")
    config.set("defaultValues", "ClearDataFile", "True")

    with open(defaultConfigFile, "w") as configFile:
        config.write(configFile)

def changeConfigFile(filename=str, id=str, content=str, type=str): # add logging
    config = configparser.ConfigParser()
    config.read(filename)

    config.set('defaultValues', str(id), str(content))

    with open(defaultConfigFile, "w") as configFile:
        config.write(configFile)

def loadConfigFile(request):
    # Create a ConfigParser object and read the config file
    config = configparser.ConfigParser()
    config.read(defaultConfigFile)

    # Retrieve the requested value from the config file
    if request == "defaultLogFile":
        value = config.get('defaultValues', 'defaultLogFile')
    elif request == "defaultDataFile":
        value = config.get('defaultValues', 'defaultDataFile')
    elif request == "defaultLogMessageType":
        value = config.get('defaultValues', 'defaultLogMessageType')
    elif request == "defaultTimerLogMessageType":
        value = config.get('defaultValues', 'defaultTimerLogMessageType')
    elif request == "defaultTimerMessage":
        value = config.get('defaultValues', 'defaultTimerMessage')
    elif request == "DebugToggle":
        value = config.getboolean('defaultValues', 'DebugToggle')
    elif request == "LogSettings":
        value = config.getboolean('defaultValues', 'LogSettings')
    elif request == "ClearLogFile":
        value = config.getboolean('defaultValues', 'ClearLogFile')
    elif request == "ClearDataFile":
        value = config.getboolean('defaultValues', 'ClearDataFile')
    else:
        raise ValueError(f"Invalid request: {request}")

    return value