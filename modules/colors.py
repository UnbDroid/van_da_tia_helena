from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


sensorColorRight = ColorSensor(Port.S2)
sensorColorLeft = ColorSensor(Port.S1)


#Declarações de métodos

def getSensorColorRight():
    return sensorColorRight.rgb()


def getSensorColorLeft():
    return sensorColorLeft.rgb()


# WHITE
# ---------------------------------------------------------------------------------------------------------------------

whiteRangeLeftR = [33, 34, 35, 36, 37]
whiteRangeLeftG = [30 ,31, 32, 33, 34]
whiteRangeLeftB = [92 ,93, 94, 95, 96]


def isWhiteLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isWhiteRangeR = valueSensorColorLeft[0] in whiteRangeLeftR
    isWhiteRangeG = valueSensorColorLeft[1] in whiteRangeLeftG
    isWhiteRangeB = valueSensorColorLeft[2] in whiteRangeLeftB

    return isWhiteRangeR and isWhiteRangeG and isWhiteRangeB


whiteRangeRightMin = [20, 23, 25]
whiteRangeRightMax = [25, 30, 30]

def isWhiteRight():
    valueSensorColorRight = getSensorColorRight()

    isWhiteRangeR = whiteRangeRightMin[0] <= valueSensorColorRight[0] <= whiteRangeRightMax[0]
    isWhiteRangeG = whiteRangeRightMin[1] <= valueSensorColorRight[1] <= whiteRangeRightMax[1]
    isWhiteRangeB = whiteRangeRightMin[2] <= valueSensorColorRight[2] <= whiteRangeRightMax[2]

    return isWhiteRangeR and isWhiteRangeG and isWhiteRangeB


def isWhite():
    return isWhiteRight() and isWhiteLeft()

# BLACK
# ---------------------------------------------------------------------------------------------------------------

blackRangeLeftR = [3, 4, 5, 6, 7]
blackRangeLeftG = [3, 4, 5, 6, 7]
blackRangeLeftB = [11 ,12, 13, 14, 15]


def isBlackLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlackRangeR = valueSensorColorLeft[0] in blackRangeLeftR
    isBlackRangeG = valueSensorColorLeft[1] in blackRangeLeftG
    isBlackRangeB = valueSensorColorLeft[2] in blackRangeLeftB

    return isBlackRangeR and isBlackRangeG and isBlackRangeB


blackRangeRightMin = [2, 2, 0]
blackRangeRightMax = [5, 5, 10]

def isBlackRight():
    valueSensorColorRight = getSensorColorRight()

    isBlackRangeR = blackRangeRightMin[0] <= valueSensorColorRight[0] <= blackRangeRightMax[0]
    isBlackRangeG = blackRangeRightMin[1] <= valueSensorColorRight[1] <= blackRangeRightMax[1]
    isBlackRangeB = blackRangeRightMin[2] <= valueSensorColorRight[2] <= blackRangeRightMax[2]

    return isBlackRangeR and isBlackRangeG and isBlackRangeB

def isBlack():
    return isBlackRight() and isBlackLeft()


# RED
# ---------------------------------------------------------------------------------------------------------------

redRangeRightR = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
redRangeRightG = [1, 2, 3, 4, 5, 6, 7]
redRangeRightB = [0, 1, 2, 3, 4]


def isRedRight():
    valueSensorColorRight = getSensorColorRight()

    isRedRangeR = valueSensorColorRight[0] in redRangeRightR
    isRedRangeG = valueSensorColorRight[1] in redRangeRightG
    isRedRangeB = valueSensorColorRight[2] in redRangeRightB

    # print('R', isRedRangeR)
    # print('G', isRedRangeG)
    # print('B', isRedRangeB)

    return isRedRangeR and isRedRangeG and isRedRangeB



redRangeLefttMin = [25, 1, 5]
redRangeLeftMax = [40, 10, 12]

def isRedLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isRedRangeR = redRangeLefttMin[0] <= valueSensorColorLeft[0] <= redRangeLeftMax[0]
    isRedRangeG = redRangeLefttMin[1] <= valueSensorColorLeft[1] <= redRangeLeftMax[1]
    isRedRangeB = redRangeLefttMin[2] <= valueSensorColorLeft[2] <= redRangeLeftMax[2]

    return isRedRangeR and isRedRangeG and isRedRangeB


def isRed():
    return isRedRight() and isRedLeft()

# BLUE
# ---------------------------------------------------------------------------------------------------------------

blueRangeLefttMin = [3, 15, 65]
blueRangeLeftMax = [8, 20, 72]

def isBlueLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlueRangeR = blueRangeLefttMin[0] <= valueSensorColorLeft[0] <= blueRangeLeftMax[0]
    isBlueRangeG = blueRangeLefttMin[1] <= valueSensorColorLeft[1] <= blueRangeLeftMax[1]
    isBlueRangeB = blueRangeLefttMin[2] <= valueSensorColorLeft[2] <= blueRangeLeftMax[2]

    return isBlueRangeR and isBlueRangeG and isBlueRangeB


blueRangeRightMin = [1, 12, 18]
blueRangeRightMax = [5, 15, 23]

def isBlueRight():
    valueSensorColorRight = getSensorColorRight()

    isBlueRangeR = blueRangeRightMin[0] <= valueSensorColorRight[0] <= blueRangeRightMax[0]
    isBlueRangeG = blueRangeRightMin[1] <= valueSensorColorRight[1] <= blueRangeRightMax[1]
    isBlueRangeB = blueRangeRightMin[2] <= valueSensorColorRight[2] <= blueRangeRightMax[2]

    return isBlueRangeR and isBlueRangeG and isBlueRangeB


def isBlue():
    return isBlueRight() and isBlueLeft()

# ---------------------------------------------------------------------------------------------------------------------

def printColorRight():
    return print('Direita: ', getSensorColorRight())


def printColorLeft():
    return print('Esquerda ', getSensorColorLeft())