# Importações : 

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from Modules.Constantes import *

sensorColorRight = ColorSensor(Port.S2)
sensorColorLeft = ColorSensor(Port.S1)

# Definindo RGB
# ---------------------------------------------------------------------------------------------------------------------------------------#


def ColorRight():
    return sensorColorRight.rgb()


def ColorLeft():
    return sensorColorLeft.rgb()
    

# Black 
# ---------------------------------------------------------------------------------------------------------------------------------------#


def is_BlackRight():
    # BLackRangeLeft é o range que foi printado
    
    isBlackR = blackRangeRightMin[0] <= ColorRight()[0] <= blackRangeRightMax[0]
    isBlackG = blackRangeRightMin[1] <= ColorRight()[1] <= blackRangeRightMax[1]
    isBlackB = blackRangeRightMin[2] <= ColorRight()[2] <= blackRangeRightMax[2]
    
    return isBlackR and isBlackG and isBlackB

def is_BlackLeft():
    isBlackR = blackRangeLeftMin[0] <= ColorLeft()[0] <= blackRangeLeftMax[0]
    isBlackG = blackRangeLeftMin[1] <= ColorLeft()[1] <= blackRangeLeftMax[1]
    isBlackB = blackRangeLeftMin[2] <= ColorLeft()[2] <= blackRangeLeftMax[2]
    
    return isBlackR and isBlackG and isBlackB

def is_Black():
    return is_BlackRight() and is_BlackLeft()


# White
# ---------------------------------------------------------------------------------------------------------------------------------------#


def is_WhiteRight():
    # whiteRangeLeft é o range que foi printado
    
    isWhiteR = whiteRangeRightMin[0] <= ColorRight()[0] <= whiteRangeRightMax[0]
    isWhiteG = whiteRangeRightMin[1] <= ColorRight()[1] <= whiteRangeRightMax[1]
    isWhiteB = whiteRangeRightMin[2] <= ColorRight()[2] <= whiteRangeRightMax[2]
    
    
    return isWhiteR and isWhiteG and isWhiteB

def is_WhiteLeft():
    isWhiteR = whiteRangeLeftMin[0] <= ColorLeft()[0] <= whiteRangeLeftMax[0]
    isWhiteG = whiteRangeLeftMin[1] <= ColorLeft()[1] <= whiteRangeLeftMax[1]
    isWhiteB = whiteRangeLeftMin[2] <= ColorLeft()[2] <= whiteRangeLeftMax[2]
    
    return isWhiteR and isWhiteG and isWhiteB

def is_White():
    return is_WhiteRight() and is_WhiteLeft()


# Red
# ------------------------------------------------------------------------------------------------------------------------ #

def is_RedRight():
    
    isRedR = redRangeRightMin[0] <= ColorRight()[0] <= redRangeRightMax[0]
    isRedG = redRangeRightMin[1] <= ColorRight()[1] <= redRangeRightMax[1]
    isRedB = redRangeRightMin[2] <= ColorRight()[2] <= redRangeRightMax[2]
    
    return isRedR and isRedG and isRedB

def is_RedLeft():
    
    isRedR = redRangeLeftMin[0] <= ColorLeft()[0] <= redRangeLeftMax[0]
    isRedG = redRangeLeftMin[1] <= ColorLeft()[1] <= redRangeLeftMax[1]
    isRedB = redRangeLeftMin[2] <= ColorLeft()[2] <= redRangeLeftMax[2]
    
    return isRedR and isRedG and isRedB

def is_Red():
    return is_RedRight() and is_RedLeft()


    


    

