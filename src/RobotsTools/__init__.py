import os
import RobotsTools.genConfigFile as gCF

if os.path.exists(gCF.dataLocation):
    pass
else:
    os.mkdir(gCF.dataLocation)

if os.path.exists(gCF.defaultConfigFile):
    pass
else:
    gCF.genConfigFile()

from RobotsTools.main import *
from RobotsTools.fileOperations import *
from RobotsTools.timerOperations import *
from RobotsTools.setSettings import *
from RobotsTools.shellIntigration import *