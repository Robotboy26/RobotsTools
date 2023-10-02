import os
#from .genConfigFile import genConfigFile
import genConfigFile

if os.path.exists(genConfigFile.dataLocation):
    pass
else:
    os.mkdir(genConfigFile.dataLocation)

if os.path.exists(genConfigFile.defaultConfigFile):
    pass
else:
    genConfigFile.genConfigFile()

from main import *
from fileOperations import *
from timerOperations import *
from shellIntigration import *
