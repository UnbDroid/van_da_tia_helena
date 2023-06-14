from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


sensorColorRight = ColorSensor(Port.S2)
sensorColorLeft = ColorSensor(Port.S1)


#Declarações de métodos

def getSensorColorRight():
    return sensorColorRight.rgb()


def getSensorColorLeft():
    return sensorColorLeft.rgb()

def printColorRight():
    return print(getSensorColorRight())


def printColorLeft():
    return print(getSensorColorLeft())

#-------------------------------------------------------------------------------
#Passado pela linha


def through_line():
    if sensorColorLeft.reflection() < 10:
        return True
    else:
        return False