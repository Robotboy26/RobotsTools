import time
import threading
defaultLogFile = "log.txt"
defaultDataFile = "data.txt"
defaultLogMessageType = "INFO"
defaultTimerLogMessageType = "TIMER"
defaultTimerMessage = "defaut timer"
DebugToggle = True
LogSettings = True
ClearLogFile = True
ClearDataFile = True

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
    global defaultLogFile
    defaultLogFile = filename
    with open(filename, "w") as file:
        if ClearLogFile == True:
            file.truncate()
        else:
            return

def Log(message=str, LogMessageType=str(defaultLogMessageType), filename=str(defaultLogFile)):
    if LogSettings == True:
        try:
            Debug(str(message), LogMessageType)
            with lock:
                with open(filename, "a") as file:
                    file.write(formattedWrite(str(message), LogMessageType))
                    file.write("\n")
        except Exception as e:
            Debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!")
    else:
        return
    
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
