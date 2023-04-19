import time
DebugToggle = True
defaultLogFile = "log.txt"

def setDebugToggle(value=bool):
    global DebugToggle
    DebugToggle = value

def Debug(message=str):
    if DebugToggle == True:
        print(message)

def LogFile(filename=str):
    global defaultLogFile
    defaultLogFile = filename
    file = open(filename, "w")
    file.truncate()
    file.close()

def changeDefaultLogFile(filename=str):
    global defaultLogFile
    defaultLogFile = filename

def Log(message=str, filename=defaultLogFile):
    file = open(filename, "a")
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    file.write(str(f"{formatted_time}   {message}"))
