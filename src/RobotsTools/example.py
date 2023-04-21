import time
DebugToggle = True
defaultLogFile = "log.txt"
defaultLogMessageType = "INFO"
defaultTimerMessage = "defaut timer"

def setDebugToggle(value=bool):
    global DebugToggle
    DebugToggle = value

def formattedWrite(message, LogMessageType=defaultLogMessageType):
    formattedTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    outMessage = str(f"[TIME:{formattedTime}] [{LogMessageType}] {message}")
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

def Log(message=str, LogMessageType=defaultLogMessageType, filename=defaultLogFile):
    Debug(str(message), LogMessageType)
    file = open(filename, "a")
    file.write(formattedWrite(str(message), LogMessageType))
    file.write("\n")

def startTimer(message=str(defaultTimerMessage)):
    global startTime
    startTime = time.time()
    formattedStartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
    Log(f"Timer {message} Started {formattedStartTime}", "TIMER", filename=defaultLogFile)

def stopTimer(message=str(defaultTimerMessage)):
    global endTime
    endTime = time.time()
    formattedEndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))
    timeTaken = endTime - startTime
    Log(f"Timer {message} Stopped {formattedEndTime} total time taken (in seconds) {timeTaken}", "TIMER", filename=defaultLogFile)
