import time
import threading
import os

from RobotsTools.genConfigFile import genConfigFile, defaultConfigFile

try:
    with open(defaultConfigFile, 'r') as file:
        pass
except:
    genConfigFile()

with open(defaultConfigFile, 'r') as file:
    fileSplitlines = []
    fileRead = file.read().splitlines()
    y = [item.split(":") for item in fileRead]
    z = [item[1].split(";") for item in y]
    y = [item[0] for item in y]
    for x in range(len(fileRead)):
        fileSplitlines.append(y[x])
        fileSplitlines.append(z[x][0])
        fileSplitlines.append(z[x][1])

    defaultLogFile = str(fileSplitlines[fileSplitlines.index("defaultLogFile") + 1])
    defaultDataFile = str(fileSplitlines[fileSplitlines.index("defaultDataFile") + 1])
    defaultLogMessageType = str(fileSplitlines[fileSplitlines.index("defaultLogMessageType") + 1])
    defaultTimerLogMessageType = str(fileSplitlines[fileSplitlines.index("defaultTimerLogMessageType") + 1])
    defaultTimerMessage = str(fileSplitlines[fileSplitlines.index("defaultTimerMessage") + 1])
    DebugToggle = bool(fileSplitlines[fileSplitlines.index("DebugToggle") + 1])
    LogSettings = bool(fileSplitlines[fileSplitlines.index("LogSettings") + 1])
    ClearLogFile = bool(fileSplitlines[fileSplitlines.index("ClearLogFile") + 1])
    ClearDataFile = bool(fileSplitlines[fileSplitlines.index("ClearDataFile") + 1])

lock = threading.Lock()

def setLogSettings(value=True):
    global LogSettings
    LogSettings = value

def setDebugToggle(value=True):
    global DebugToggle
    DebugToggle = value

def setClearLogFile(value=True):
    global ClearLogFile
    ClearLogFile = value

def setClearDataFile(value=True):
    global ClearDataFile
    ClearDataFile = value

def changeDefaultLogFile(filename=str):
    global defaultLogFile
    defaultLogFile = filename

def formattedWrite(message, LogMessageType=defaultLogMessageType):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[{formattedTime}] [{LogMessageType}] {message}")
    return outMessage


def Debug(message=str, LogMessageType=defaultLogMessageType):
    if DebugToggle == True:
        print(formattedWrite(message, LogMessageType))

def LogFile(filename=str, ClearLogFile=bool(ClearLogFile)):
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

def Log(message=str, LogMessageType=str(defaultLogMessageType), filename=str(defaultLogFile)):
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
    
def LogList(message=str, LogMessageType=str(defaultLogMessageType), filename=str(defaultLogFile)):
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
