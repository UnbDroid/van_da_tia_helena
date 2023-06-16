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

whiteRangeLeftR = [31, 32, 33, 34, 35, 36, 37]
whiteRangeLeftG = [28, 29, 30 ,31, 32, 33, 34, 35, 36]
whiteRangeLeftB = [90, 89 ,88, 87, 86, 85, 84]


def isWhiteLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isWhiteRangeR = valueSensorColorLeft[0] in whiteRangeLeftR
    isWhiteRangeG = valueSensorColorLeft[1] in whiteRangeLeftG
    isWhiteRangeB = valueSensorColorLeft[2] in whiteRangeLeftB

    return isWhiteRangeR and isWhiteRangeG and isWhiteRangeB


whiteRangeRightMin = [35, 30, 95]
whiteRangeRightMax = [45, 40, 105]

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

blackRangeLeftR = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]
blackRangeLeftG = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]
blackRangeLeftB = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]


def isBlackLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlackRangeR = valueSensorColorLeft[0] in blackRangeLeftR
    isBlackRangeG = valueSensorColorLeft[1] in blackRangeLeftG
    isBlackRangeB = valueSensorColorLeft[2] in blackRangeLeftB

    return isBlackRangeR and isBlackRangeG and isBlackRangeB


blackRangeRightMin = [1, 2, 3]
blackRangeRightMax = [12, 20, 12]

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

# redRangeRightR = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
# redRangeRightG = [1, 2, 3, 4, 5, 6, 7]
# redRangeRightB = [0, 1, 2, 3, 4]

redRangeRightR = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
redRangeRightG = [1, 2, 3, 4, 5, 6, 7]
redRangeRightB = [7, 8, 9, 10, 11, 12, 13, 14]


def isRedRight():
    valueSensorColorRight = getSensorColorRight()

    isRedRangeR = valueSensorColorRight[0] in redRangeRightR
    isRedRangeG = valueSensorColorRight[1] in redRangeRightG
    isRedRangeB = valueSensorColorRight[2] in redRangeRightB

    # print('R', isRedRangeR)
    # print('G', isRedRangeG)
    # print('B', isRedRangeB)

    return isRedRangeR and isRedRangeG and isRedRangeB



redRangeLefttMin = [25, 1, 2]
redRangeLeftMax = [40, 10, 12]

def isRedLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isRedRangeR = redRangeLefttMin[0] <= valueSensorColorLeft[0] <= redRangeLeftMax[0]
    isRedRangeG = redRangeLefttMin[1] <= valueSensorColorLeft[1] <= redRangeLeftMax[1]
    isRedRangeB = redRangeLefttMin[2] <= valueSensorColorLeft[2] <= redRangeLeftMax[2]

    # print('R', isRedRangeR)
    # print('G', isRedRangeG)
    # print('B', isRedRangeB)

    return isRedRangeR and isRedRangeG and isRedRangeB


def isRed():
    return isRedRight() and isRedLeft()

# BLUE
# ---------------------------------------------------------------------------------------------------------------

blueRangeLefttMin = [3, 11, 55]
blueRangeLeftMax = [8, 20, 65]

def isBlueLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlueRangeR = blueRangeLefttMin[0] <= valueSensorColorLeft[0] <= blueRangeLeftMax[0]
    isBlueRangeG = blueRangeLefttMin[1] <= valueSensorColorLeft[1] <= blueRangeLeftMax[1]
    isBlueRangeB = blueRangeLefttMin[2] <= valueSensorColorLeft[2] <= blueRangeLeftMax[2]

    return isBlueRangeR and isBlueRangeG and isBlueRangeB


blueRangeRightMin = [1, 12, 78]
blueRangeRightMax = [10, 20, 85]

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