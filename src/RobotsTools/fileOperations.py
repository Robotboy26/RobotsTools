from RobotsTools.main import *


def loadFile(filename=str, mode=str("r")):
    with open(str(filename), mode) as file:
        fileContent = file.read().splitlines()
    Log(f"Loaded file '{filename}' with content '{fileContent}'", "FILE LOAD")
    return fileContent

def saveFile(filename=str, content=str, mode=str("w")):
    with open(str(filename), mode) as file:
        file.write(content)
    Log(f"Saved file '{filename}' with content '{content}'", "FILE WRITE")

def writeToFile(filename=str, content=str, newline=bool(True), mode=str("a"),):
    try:
        with open(str(filename), mode) as file:
            file.write(str(content))
            if newline == True:
                file.write("\n")
        Log(f"Wrote '{str(content)}' to file '{filename}'", "FILE WRITE")
    except FileNotFoundError:
        Log(f"!!! Could not write to file '{filename}' it was not found!!!", "FILE ERROR")

    except:
        Log(f"!!! Could not write to file '{filename}', unknown error!!!", "FILE ERROR")


def generateDataFile(data, filename=str(loadConfigFile("defaultDataFile")), mode=str("a")):
    with open(filename, "w") as file:
        if ClearDataFile == True:
            file.truncate()
        else:
            pass
    if isinstance(data, list):
        with open(filename, mode) as file:
            for x in range(len(data)):
                file.write(f"{[var for var in globals() if globals()[var] is data][0]};{x}:{data[x]}\n")
    elif isinstance(data, str):
        with open(filename, mode) as file:
            file.write(f"{[var for var in globals() if globals()[var] is data][0]}:{data}")
    else:
        Debug("!!!   invalid data type   !!!", "ERROR")



def createSimpleConfigFile(filename=str):
    try:
        with open(str(filename), 'r') as file:
            pass
    except FileNotFoundError:
        try:
            with open(str(filename), "w") as file:
                file.write(f"filename: '{filename}'")
                file.write("\n")
            Log(f"Created config file '{filename}'", "FILE CREATION")
        except:
            Log(f"!!! Could not create config file '{filename}', unknown error!!!", "FILE ERROR")

def addToSimpleConfigFile(filename=str, id=[str, int], content=str, newline=bool(True)): # if trying to add a line that is the same a a line already in the file run an error instead of adding it anyway
    try:
        with open(str(filename), "r") as file:
            fileContent = file.read().splitlines()
            fileContent.index(f"{str(id)}: '{str(content)}'")
            Log(f"Could not add to config file '{filename}' it already contains '{str(content)}' at {str(id)}", "SOFT FILE ERROR")
            return
    except ValueError:
        with open(str(filename), "a") as file:
            file.write(f"{str(id)}: '{str(content)}'")
            if newline == True:
                file.write("\n")
        Log(f"Added '{str(content)}' to config file '{filename}'", "FILE EDIT")
    except FileNotFoundError:
        Log(f"!!! Could not add to config file '{filename}' it was not found!!!", "FILE ERROR")

    except:
        Log(f"!!! Could not add to config file '{filename}', unknown error!!!", "FILE ERROR")

def removeFromSimpleConfigFile(filename=str, id=[str, int]):
    pass

def getFromSimpleConfigFile(filename=str, id=[str, int]):
    try:
        returnList = []
        with open(str(filename), "r") as file:
            fileContent = file.read().splitlines()
        for line in fileContent:
            if str(id) in line:
                value = line.split("'")[1]
                returnList.append(line)
        if len(returnList) == 1:
            returnList = str(returnList)
        Log(f"Got '{str(returnList)}' from config file '{filename}'", "FILE GET")
        return returnList
    except:
        Log(f"!!! Could not get from config file '{filename}', unknown error!!!", "FILE ERROR")
                

def loadSimpleConfigFile(filename=str):
    pass
        