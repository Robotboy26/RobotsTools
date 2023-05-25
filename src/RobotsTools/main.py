import time
import threading
import os

from RobotsTools.genConfigFile import *

try:
    with open(defaultConfigFile, 'r') as file:
        pass
except:
    genConfigFile()

lock = threading.Lock()

def setLogSettings(value=True):
    changeConfigFile(defaultConfigFile, "LogSettings", value, "Str")
    Log(getConfigValue("LogSettings"), "CONFIG CHANGE")

def setDebugToggle(value=True):
    changeConfigFile(defaultConfigFile, "DebugToggle", value, "Str")
    Log(getConfigValue("DebugToggle"), "CONFIG CHANGE")

def setClearLogFile(value=True):
    changeConfigFile(defaultConfigFile, "ClearLogFile", value, "Str")
    Log(getConfigValue("ClearLogFile"), "CONFIG CHANGE")

def setClearDataFile(value=True):
    changeConfigFile(defaultConfigFile, "ClearDataFile", value, "Str")
    Log(getConfigValue("ClearDataFile"), "CONFIG CHANGE")

def changeDefaultLogFile(filename=str):
    changeConfigFile(defaultConfigFile, "defaultLogFile", filename, "Str")
    Log(getConfigValue("defaultLogFile"), "CONFIG CHANGE")


def formattedWrite(message, LogMessageType=getConfigValue("defaultLogMessageType")):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[{formattedTime}] [{LogMessageType}] {message}")
    return outMessage


def Debug(message=str, LogMessageType=getConfigValue("defaultLogMessageType")):
    if getConfigValue("DebugToggle") == True:
        print(formattedWrite(message, LogMessageType))

def LogFile(filename=str, ClearLogFile=bool(getConfigValue("ClearLogFile"))):
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

def Log(message=str, LogMessageType=str(getConfigValue("defaultLogMessageType")), filename=str(getConfigValue("defaultLogFile"))):
    LogMessageType = LogMessageType.upper()
    if getConfigValue("LogSettings") == True:
        try:
            Debug(str(message), LogMessageType)
            with lock:
                with open(filename, "a") as file:
                    file.write(formattedWrite(str(message), LogMessageType))
                    file.write("\n")
            return "Log secceeded"
        except Exception as e:
            Debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!")
            return e
    else:
        return "LogSettings is False"
    
def LogList(message=str, LogMessageType=str(getConfigValue("defaultLogMessageType")), filename=str(getConfigValue("defaultLogFile"))):
    if getConfigValue("LogSettings") == True:
        try:
            for x in range(len(message)):
                Debug(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType)
                with open(filename, "a") as file:
                    file.write(formattedWrite(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType))
                    file.write("\n")
            return
        except Exception as e:
            Debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!", "ERROR")
    else:
        return
