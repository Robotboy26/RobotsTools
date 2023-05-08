from RobotsTools.main import *

def startTimer(message=str(loadConfigFile("defaultTimerMessage")), LogMessageType=str(loadConfigFile("defaultTimerLogMessageType")), filename=str(loadConfigFile("defaultLogFile"))):
    global startTime
    startTime = time.time()
    formattedStartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
    Log(f"Timer '{message}' Started {formattedStartTime}", LogMessageType, filename)

def stopTimer(message=str(loadConfigFile("defaultTimerMessage")), LogMessageType=str(loadConfigFile("defaultTimerLogMessageType")), filename=str(loadConfigFile("defaultLogFile"))):
    global endTime
    endTime = time.time()
    formattedEndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))
    timeTaken = endTime - startTime
    Log(f"Timer '{message}' Stopped {formattedEndTime} total time taken (in seconds) {timeTaken}", LogMessageType, filename)
