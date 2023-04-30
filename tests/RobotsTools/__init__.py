import os
from RobotsTools.genConfigFile import genConfigFile, defaultConfigFile

if os.path.exists(defaultConfigFile):
    pass
else:
    genConfigFile()

from RobotsTools.main import *
from RobotsTools.fileOperations import *
from RobotsTools.timerOperations import *