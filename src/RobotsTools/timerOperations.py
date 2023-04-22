from RobotsTools.main import *

def startTimer(message=str(defaultTimerMessage)):
    global startTime
    startTime = time.time()
    formattedStartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(startTime))
    Log(f"Timer '{message}' Started {formattedStartTime}", "TIMER", filename=defaultLogFile)

def stopTimer(message=str(defaultTimerMessage)):
    global endTime
    endTime = time.time()
    formattedEndTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endTime))
    timeTaken = endTime - startTime
    Log(f"Timer '{message}' Stopped {formattedEndTime} total time taken (in seconds) {timeTaken}", "TIMER", filename=defaultLogFile)
