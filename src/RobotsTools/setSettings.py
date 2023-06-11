from .genConfigFile import defaultConfigFile
from .fileOperations import addToConfigFile


def setLogSettings(value=True):
    addToConfigFile(defaultConfigFile, "LogSettings", value, "default")

def setDebugToggle(value=True):
    addToConfigFile(defaultConfigFile, "DebugToggle", value, "default")

def setClearLogFile(value=True):
    addToConfigFile(defaultConfigFile, "ClearLogFile", value, "default")

def setClearDataFile(value=True):
    addToConfigFile(defaultConfigFile, "ClearDataFile", value, "default")

def changeDefaultLogFile(filename=str):
    addToConfigFile(defaultConfigFile, "defaultLogFile", filename, "default")