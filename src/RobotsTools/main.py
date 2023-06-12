import time
import threading
import os

from .genConfigFile import genConfigFile, defaultConfigFile, getConfigValue

try:
    with open(defaultConfigFile, 'r') as file:
        pass
except:
    genConfigFile()

lock = threading.Lock()

from .setSettings import changeDefaultLogFile

def logFile(filename=str, ClearLogFile=bool(getConfigValue("ClearLogFile"))):
    changeDefaultLogFile(filename)
    if os.path.exists(filename):
        if ClearLogFile == True:
            with open(filename, 'w') as file:
                file.truncate(0)
            return "File exists truncated"
        else:
            return "File exists not truncated"
    else:
        with open(filename, 'w') as file:
            pass
        return "File created"
    
def truncateLogFile(filename=str):
    with open(filename, 'w') as file:
        file.truncate(0)

def LogList(message=str, LogMessageType=str(getConfigValue("defaultLogMessageType")), filename=str(getConfigValue("defaultLogFile"))):
    if getConfigValue("LogSettings") == True:
        try:
            for x in range(len(message)):
                debug(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType)
                with open(filename, "a") as file:
                    file.write(formattedWrite(f"{str(message[x])} as index {str(x)} of list {[var for var in globals() if globals()[var] is message][0]}", LogMessageType))
                    file.write("\n")
            return
        except Exception as e:
            debug(f"!!! Could not log: {str(e)}, you might need to setLogSettings !!!", "ERROR")
    else:
        return
