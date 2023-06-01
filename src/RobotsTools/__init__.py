import os
import RobotsTools.genConfigFile as gCF

if os.path.exists(gCF.dataLocation):
    pass
else:
    os.mkdir(dataLocation)

if os.path.exists(defaultConfigFile):
    pass
else:
    gCF.genConfig()

from RobotsTools.main import *
from RobotsTools.fileOperations import *
from RobotsTools.timerOperations import *