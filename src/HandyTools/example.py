import time
DebugToggle = True
defaultLogFile = "log.txt"
defaultLogMessageType = "INFO"
timerCount = 0

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
    Debug(message, LogMessageType)
    file = open(filename, "a")
    file.write(formattedWrite(message, LogMessageType))
    file.write("\n")

def startTimer(message=str(timerCount)):
    global timerCount
    global startTime
    startTime = time.time()
    formattedStartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
    Log(f"Timer {message} Started {formattedStartTime}", "TIMER", filename=defaultLogFile)
    timerCount = timerCount + 1

def stopTimer(message=str(timerCount)):
    global endTime
    endTime = time.time()
    formattedEndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))
    timeTaken = endTime - startTime
    Log(f"Timer {message} Stopped {formattedEndTime} total time taken (in seconds) {timeTaken}", "TIMER", filename=defaultLogFile)
