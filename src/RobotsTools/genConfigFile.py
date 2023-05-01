defaultConfigFile = "RobotToolsConfig.txt" # do not change unless you also change in main.py

def genConfigFile():
    with open(defaultConfigFile, 'w') as file:
        pass

    with open(defaultConfigFile, 'a') as file:
        file.write("DebugToggle:True;Bool\n")
        file.write("LogSettings:True;Bool\n")
        file.write("ClearLogFile:True;Bool\n")
        file.write("ClearDataFile:True;Bool\n")
        file.write("defaultLogFile:logfile.txt;Str\n")
        file.write("defaultDataFile:datafile.txt;Str\n")
        file.write("defaultLogMessageType:INFO;Str\n")
        file.write("defaultTimerLogMessageType:TIMER;Str\n")
        file.write("defaultTimerMessage:default timer;Str\n")

def changeConfigFile(filename=str, id=str, content=str, type=str): # add logging
    with open(filename, 'r') as file:
        fileContent = file.read().splitlines()

    for x in range(len(fileContent)):
        if fileContent[x].split(";")[0] == id:
            fileContent[x] = f"{id}:{content};{type}"
            break

    with open(filename, 'w') as file:
        for x in range(len(fileContent)):
            file.write(f"{fileContent[x]}\n")

def loadConfigFile(request):
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

        with open(defaultConfigFile, 'r') as file:    
            configDataPoints = file.read().splitlines()
        configDataLocation = []

        defaultLogFile = str(fileSplitlines[fileSplitlines.index("defaultLogFile") + 1])
        defaultDataFile = str(fileSplitlines[fileSplitlines.index("defaultDataFile") + 1])
        defaultLogMessageType = str(fileSplitlines[fileSplitlines.index("defaultLogMessageType") + 1])
        defaultTimerLogMessageType = str(fileSplitlines[fileSplitlines.index("defaultTimerLogMessageType") + 1])
        defaultTimerMessage = str(fileSplitlines[fileSplitlines.index("defaultTimerMessage") + 1])
        DebugToggle = bool(fileSplitlines[fileSplitlines.index("DebugToggle") + 1])

        LogSettings = bool(fileSplitlines[fileSplitlines.index("LogSettings") + 1])
        ClearLogFile = bool(fileSplitlines[fileSplitlines.index("ClearLogFile") + 1])
        ClearDataFile = bool(fileSplitlines[fileSplitlines.index("ClearDataFile") + 1])
        requestInfo = locals()[request]
        return requestInfo