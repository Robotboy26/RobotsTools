import time
defaultLogFile = "log.txt"
defaultLogMessageType = "INFO"
defaultTimerMessage = "defaut timer"
DebugToggle = True
LogSettings = True

def setLogSettings(value=True):
    global LogSettings
    LogSettings = value

def setDebugToggle(value=True):
    global DebugToggle
    DebugToggle = value

def formattedWrite(message, LogMessageType=defaultLogMessageType):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[{formattedTime}] [{LogMessageType}] {message}")
    return outMessage


def Debug(message=str, LogMessageType=defaultLogMessageType):
    if DebugToggle == True:
        print(formattedWrite(message, LogMessageType))

def LogFile(filename=str):
    global defaultLogFile
    defaultLogFile = filename
    file = open(filename, "w")
    file.truncate()
    file.close()

def changeDefaultLogFile(filename=str):
    global defaultLogFile
    defaultLogFile = filename

def Log(message=str, LogMessageType=str(defaultLogMessageType), filename=str(defaultLogFile)):
    if LogSettings == True:
        try:
            Debug(str(message), LogMessageType)
            file = open(filename, "a")
            file.write(formattedWrite(str(message), LogMessageType))
            file.write("\n")
        except Exception as e:
            Debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!")
    else:
        return