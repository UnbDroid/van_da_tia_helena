from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


sensorColorRight = ColorSensor(Port.S2)
sensorColorLeft = ColorSensor(Port.S1)


#Declarações de métodos

def getSensorColorRight():
    return sensorColorRight.rgb()


def getSensorColorLeft():
    return sensorColorLeft.rgb()


# ----------------------------------------------------------------------------------------------------------------------------------------------
#Primeira possível solução

blueRangeLeftR = [3, 4, 5, 6, 7]
blueRangeLeftG = [13 ,14, 15, 16, 17]
blueRangeLeftB = [62 ,63, 64, 65, 66]


def isBlueLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlueRangeR = valueSensorColorLeft[0] in blueRangeLeftR
    isBlueRangeG = valueSensorColorLeft[1] in blueRangeLeftG
    isBlueRangeB = valueSensorColorLeft[2] in blueRangeLeftB

    return isBlueRangeR and isBlueRangeG and isBlueRangeB



# ----------------------------------------------------------------------------------------------------------------------------------------------
#Segunda possível solução

blueRangeRightMin = [3, 13, 20]
blueRangeRightMax = [5, 15, 22]

def isBlueRight():
    valueSensorColorRight = getSensorColorRight()

    isBlueRangeR = blueRangeRightMin[0] <= valueSensorColorRight[0] <= blueRangeRightMax[0]
    isBlueRangeG = blueRangeRightMin[1] <= valueSensorColorRight[1] <= blueRangeRightMax[1]
    isBlueRangeB = blueRangeRightMin[2] <= valueSensorColorRight[2] <= blueRangeRightMax[2]

    return isBlueRangeR and isBlueRangeG and isBlueRangeB


def printColorRight():
    return print(getSensorColorRight())


def printColorLeft():
    return print(getSensorColorLeft())
