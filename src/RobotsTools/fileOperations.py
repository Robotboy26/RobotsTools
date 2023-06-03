import configparser
from main import log, debug
from genConfigFile import getConfigValue

# in the config file make it for .ini files instead of how it is now

def loadFile(filename=str, mode=str("r")):
    with open(str(filename), mode) as file:
        fileContent = file.read().splitlines()
    log(f"Loaded file '{filename}' with content '{fileContent}'", "FILE LOAD")
    return fileContent

def saveFile(filename=str, content=str, mode=str("w")):
    with open(str(filename), mode) as file:
        file.write(content)
    log(f"Saved file '{filename}' with content '{content}'", "FILE WRITE")

# fix these with the new config file system

def writeToFile(filename=str, content=str, newline=bool(True), mode=str("a"),):
    try:
        with open(str(filename), mode) as file:
            file.write(str(content))
            if newline == True:
                file.write("\n")
        log(f"Wrote '{str(content)}' to file '{filename}'", "FILE WRITE")
    except FileNotFoundError:
        log(f"!!! Could not write to file '{filename}' it was not found!!!", "FILE ERROR")

    except:
        log(f"!!! Could not write to file '{filename}', unknown error!!!", "FILE ERROR")


def generateDataFile(data, filename=str(getConfigValue("defaultDataFile")), mode=str("a")):
    with open(filename, "w") as file:
        if getConfigValue("ClearDataFile") == True:
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
        debug("!!!   invalid data type   !!!", "ERROR")



def createConfigFile(filename=str):
    if filename[-4:] == ".ini":
        pass
    if filename[-4:] == ".txt":
        quit("!!!   config file cannot be a .txt file (change it to .ini)   !!!")
    if "." not in filename:
        if filename[-3:] == "ini":
            quit("!!!   config file is missing a . (change it to .ini)   !!!")
        if filename[-3:] == "txt":
            quit("!!!   config file is missing a . and has txt instead of ini (change it to .ini)   !!!")
        filename = filename + ".ini"
        log("needed to add .ini to the end of the config file name (plz add it in the code)", "FILE WARNING")

    try:
        with open(str(filename), 'r') as file:
            pass
    except FileNotFoundError:
        try:
            config = configparser.ConfigParser()
            config.read(filename)
            section = "internal"
            config.add_section(section)
            
            config.set(section, "filename", filename)

            with open(filename, "w") as configFile:
                configFile.write(config.write(configFile))
                log(f"created config file {filename}", "FILE CREATED")
        except Exception as e:
            log(f"!!! Could not create config file '{filename}', error {e} !!!", "FILE ERROR")

def addToConfigFile(filename=str, id=[str, int], content=str, section=str("config")): # if trying to add a line that is the same a a line already in the file run an error instead of adding it anyway
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        if config.has_section(section):
            pass
        else:
            config.add_section(section)

        config.set(section, str(id), str(content))
        with open(filename, "w") as configFile:
                configFile.write(config.write(configFile))
        log(f"Added '{str(content)}' to config file '{filename}'", "FILE EDIT")
        return
    except FileNotFoundError:
        log(f"!!! Could not add to config file '{filename}' it was not found!!!", "FILE ERROR")

    except Exception as e:
        log(f"!!! Could not add to config file '{filename}', error {e} !!!", "FILE ERROR")

def removeFromConfigFile(filename=str, id=[str, int]):
    pass

def getFromConfigFile(filename=str, id=[str, int] , section=str("config")):
    try:
        config = configparser.ConfigParser()
        config.read(filename)

        value = config.get(section, id)
    except Exception as e:
        quit(f"!!! Could not get from config file, error: {e} !!!")

    return value        
