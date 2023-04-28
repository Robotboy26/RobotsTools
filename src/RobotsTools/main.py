import time
import threading
import os

with open("RobotToolsConfig.txt") as file:
    defaultLogFile = str(file.read().splitlines[file.read().splitlines.index("defaultLogFile")].split(":")[1].split(";")[0])
    defaultDataFile = str(file.read().splitlines[file.read().splitlines.index("defaultDataFile")].split(":")[1].split(";")[0])
    defaultLogMessageType = str(file.read().splitlines[file.read().splitlines.index("defaultLogMessageType")].split(":")[1].split(";")[0])
    defaultTimerLogMessageType = str(file.read().splitlines[file.read().splitlines.index("defaultTimerLogMessageType")].split(":")[1].split(";")[0])
    defaultTimerMessage = str(file.read().splitlines[file.read().splitlines.index("defaultTimerMessage")].split(":")[1].split(";")[0])
    DebugToggle = bool(file.read().splitlines[file.read().splitlines.index("DebugToggle")].split(":")[1].split(";")[0])
    LogSettings = bool(file.read().splitlines[file.read().splitlines.index("LogSettings")].split(":")[1].split(";")[0])
    ClearLogFile = bool(file.read().splitlines[file.read().splitlines.index("ClearLogFile")].split(":")[1].split(";")[0])
    ClearDataFile = bool(file.read().splitlines[file.read().splitlines.index("ClearDataFile")].split(":")[1].split(";")[0])

def test():
    print(defaultLogFile)
    print(defaultDataFile)
    print(defaultLogMessageType)
    print(defaultTimerLogMessageType)
    print(defaultTimerMessage)
    print(DebugToggle)
    print(LogSettings)
    print(ClearLogFile)
    print(ClearDataFile)

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
