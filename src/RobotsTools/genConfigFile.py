import configparser
defaultConfigFile = "RobotToolsConfig.ini" # do not change unless you also change in main.py

def genConfigFile():
    config = configparser.ConfigParser()
    defaultSection = 'default'
    config.add_section(defaultSection)
    
    config.set(defaultSection, "defaultLogFile", "logFile.txt")
    config.set(defaultSection, "defaultDataFile", "dataFile.txt")
    config.set(defaultSection, "defaultLogMessageType", "INFO")
    config.set(defaultSection, "defaultTimerLogMessageType", "TIMER")
    config.set(defaultSection, "defaultTimerMessage", "default timer")
    config.set(defaultSection, "DebugToggle", "True")
    config.set(defaultSection, "LogSettings", "True")
    config.set(defaultSection, "ClearLogFile", "True")
    config.set(defaultSection, "ClearDataFile", "True")

    with open(defaultConfigFile, "w") as configFile:
        config.write(configFile)

def changeConfigFile(filename=str, id=str, content=str, type=str): # add logging
    config = configparser.ConfigParser()
    config.read(filename)

    config.set('defaultValues', str(id), str(content))

    with open(defaultConfigFile, "w") as configFile:
        config.write(configFile)

def getConfigValue(request, section='default'):
    # Create a ConfigParser object and read the config file
    config = configparser.ConfigParser()
    config.read(defaultConfigFile)

    try:
        value = config.get(section, request)
    except Exception as e:
        quit(f"!!! Could not load config file, error: {e} !!!")

    return value