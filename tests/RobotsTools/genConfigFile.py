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
        if fileContent[x].split(":")[0] == id:
            fileContent[x] = f"{id}:{content};{type}"
            break

    with open(filename, 'w') as file:
        for x in range(len(fileContent)):
            file.write(f"{fileContent[x]}\n")