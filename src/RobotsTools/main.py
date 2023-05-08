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

def setLogSettings(value=True):     # change a value in the config file
    global LogSettings
    LogSettings = value

def setDebugToggle(value=True):     # change a value in the config file
    global DebugToggle
    DebugToggle = value

def setClearLogFile(value=True):     # change a value in the config file
    global ClearLogFile
    ClearLogFile = value

def setClearDataFile(value=True):     # change a value in the config file
    global ClearDataFile
    ClearDataFile = value

def changeDefaultLogFile(filename=str):     # change a value in the config file
    changeConfigFile(defaultConfigFile, "defaultLogFile", filename, "Str")
    print(loadConfigFile("defaultLogFile"))


def formattedWrite(message, LogMessageType=loadConfigFile("defaultLogMessageType")):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[{formattedTime}] [{LogMessageType}] {message}")
    return outMessage


def Debug(message=str, LogMessageType=loadConfigFile("defaultLogMessageType")):
    if DebugToggle == True:
        print(formattedWrite(message, LogMessageType))

def LogFile(filename=str, ClearLogFile=bool(loadConfigFile("ClearLogFile"))):
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

def Log(message=str, LogMessageType=str(loadConfigFile("defaultLogMessageType")), filename=str(loadConfigFile("defaultLogFile"))):
    if LogSettings == True:
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
    
def LogList(message=str, LogMessageType=str(loadConfigFile("defaultLogMessageType")), filename=str(loadConfigFile("defaultLogFile"))):
    if LogSettings == True:
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
