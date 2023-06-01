import time
import threading
import os

import RobotsTools.genConfigFile as gCF

try:
    with open(gCF.defaultConfigFile, 'r') as file:
        pass
except:
    gCF.genConfigFile()

lock = threading.Lock()

def setLogSettings(value=True):
    gCF.changeConfigFile(gCF.defaultConfigFile, "LogSettings", value, "Str")
    log(gCF.getConfigValue("LogSettings"), "CONFIG CHANGE")

def setDebugToggle(value=True):
    gCF.changeConfigFile(gCF.defaultConfigFile, "DebugToggle", value, "Str")
    log(gCF.getConfigValue("DebugToggle"), "CONFIG CHANGE")

def setClearLogFile(value=True):
    gCF.changeConfigFile(gCF.defaultConfigFile, "ClearLogFile", value, "Str")
    log(gCF.getConfigValue("ClearLogFile"), "CONFIG CHANGE")

def setClearDataFile(value=True):
    gCF.changeConfigFile(gCF.defaultConfigFile, "ClearDataFile", value, "Str")
    log(gCF.getConfigValue("ClearDataFile"), "CONFIG CHANGE")

def changeDefaultLogFile(filename=str):
    gCF.changeConfigFile(gCF.defaultConfigFile, "defaultLogFile", filename, "Str")
    log(gCF.getConfigValue("defaultLogFile"), "CONFIG CHANGE")


def formattedWrite(message, LogMessageType=gCF.getConfigValue("defaultLogMessageType")):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[{formattedTime}] [{LogMessageType}] {message}")
    return outMessage


def debug(message=str, LogMessageType=gCF.getConfigValue("defaultLogMessageType")):
    if gCF.getConfigValue("DebugToggle") == True:
        print(formattedWrite(message, LogMessageType))

def logFile(filename=str, ClearLogFile=bool(gCF.getConfigValue("ClearLogFile"))):
    changeDefaultLogFile(filename)
    if os.path.exists(filename):
        if ClearLogFile == True:
            with open(filename, 'w') as file:
                file.truncate(0)
            return "File exists truncated"
        else:
            return "File exists not truncated"
    else:
        with open(filename, 'w') as file:
            pass
        return "File created"
    
def truncateLogFile(filename=str):
    with open(filename, 'w') as file:
        file.truncate(0)


def log(message=str, LogMessageType=str(gCF.getConfigValue("defaultLogMessageType")), filename=str(gCF.getConfigValue("defaultLogFile"))):
    LogMessageType = LogMessageType.upper()
    if gCF.getConfigValue("LogSettings") == True:
        try:
            debug(str(message), LogMessageType)
            with lock:
                with open(filename, "a") as file:
                    file.write(formattedWrite(str(message), LogMessageType))
                    file.write("\n")
            return "log secceeded"
        except Exception as e:
            debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!")
            return e
    else:
        return "LogSettings is False"
    
def LogList(message=str, LogMessageType=str(gCF.getConfigValue("defaultLogMessageType")), filename=str(gCF.getConfigValue("defaultLogFile"))):
    if gCF.getConfigValue("LogSettings") == True:
        try:
            for x in range(len(message)):
                debug(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType)
                with open(filename, "a") as file:
                    file.write(formattedWrite(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType))
                    file.write("\n")
            return
        except Exception as e:
            debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!", "ERROR")
    else:
        return
