import os
from RobotsTools.genConfigFile import genConfigFile, defaultConfigFile, dataLocation

if os.path.exists(dataLocation):
    pass
else:
    os.mkdir(dataLocation)

if os.path.exists(defaultConfigFile):
    pass
else:
    genConfigFile()

from RobotsTools.main import *
from RobotsTools.fileOperations import *
from RobotsTools.timerOperations import *