import configparser
dataLocation = "RobotsToolsData"
defaultConfigFile = f"{dataLocation}/RobotToolsConfig.ini" # do not change unless you also change in main.py
defaultSection = 'default'


def genConfigFile():
    configFileGlobal = configparser.ConfigParser()
    configFileGlobal.add_section(defaultSection)
    
    configFileGlobal.set(defaultSection, "defaultLogFile", "logFile.txt")
    configFileGlobal.set(defaultSection, "defaultDataFile", "dataFile.txt")
    configFileGlobal.set(defaultSection, "defaultLogMessageType", "INFO")
    configFileGlobal.set(defaultSection, "defaultTimerLogMessageType", "TIMER")
    configFileGlobal.set(defaultSection, "defaultTimerMessage", "default timer")
    configFileGlobal.set(defaultSection, "DebugToggle", "True")
    configFileGlobal.set(defaultSection, "LogSettings", "True")
    configFileGlobal.set(defaultSection, "ClearLogFile", "True")
    configFileGlobal.set(defaultSection, "ClearDataFile", "True")

    with open(defaultConfigFile, "w") as configFile:
        configFileGlobal.write(configFile)

def changeConfigFile(filename=str, id=str, content=str, type=str): # add logging
    configFileGlobal = configparser.ConfigParser()
    configFileGlobal.read(filename)

    configFileGlobal.set(defaultSection, str(id), str(content))

    with open(defaultConfigFile, "w") as configFile:
        configFile.write(configFileGlobal.write(configFile))

def getConfigValue(request, section=defaultSection):
    # Create a ConfigParser object and read the config file
    try:
        configFileGlobal = configparser.ConfigParser()
        configFileGlobal.read(defaultConfigFile)

        value = configFileGlobal.get(section, request)
    except Exception as e:
        quit(f"!!! Could not load config file, error: {e} !!! {request}")

    return value