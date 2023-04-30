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