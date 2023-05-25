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
    try:
        value = config.get('defaultValues', str(request))
    except Exception as e:
        raise ValueError(f"Invalid request: {e}")

    return value