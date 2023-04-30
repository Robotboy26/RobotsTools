from RobotsTools.main import *

def startTimer(message=str(defaultTimerMessage), LogMessageType=str(defaultTimerLogMessageType), filename=str(defaultLogFile)):
    global startTime
    startTime = time.time()
    formattedStartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
    Log(f"Timer '{message}' Started {formattedStartTime}", LogMessageType, filename)

def stopTimer(message=str(defaultTimerMessage), LogMessageType=str(defaultTimerLogMessageType), filename=str(defaultLogFile)):
    global endTime
    endTime = time.time()
    formattedEndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))
    timeTaken = endTime - startTime
    Log(f"Timer '{message}' Stopped {formattedEndTime} total time taken (in seconds) {timeTaken}", LogMessageType, filename)
