#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# Declaraçoes de variáveis

ev3 = EV3Brick()
sensorColorRight =  ColorSensor(Port.S3)
sensorColorLeft = ColorSensor(Port.S4)


#Declarações de métodos

def getSensorColorRight():
    return sensorColorRight.rgb()


def getSensorColorLeft():
    return sensorColorLeft.rgb()


# ----------------------------------------------------------------------------------------------------------------------------------------------
#Primeira possível solução

blueRangeLeftR = [5, 6, 7, 8, 9, 10]
blueRangeLeftG = [27, 28, 29, 30, 31]
blueRangeLeftB = [45, 46, 47, 48, 49]


def isBlueLeft():
    valueSensorColorLeft = getSensorColorLeft()

    isBlueRangeR = valueSensorColorLeft[0] in blueRangeLeftR
    isBlueRangeG = valueSensorColorLeft[1] in blueRangeLeftG
    isBlueRangeB = valueSensorColorLeft[2] in blueRangeLeftB

    return isBlueRangeR and isBlueRangeG and isBlueRangeB



# ----------------------------------------------------------------------------------------------------------------------------------------------
#Segunda possível solução

blueRangeRightMin = [6, 28, 46]
blueRangeRightMax = [12, 33, 55]

def isBlueRight():
    valueSensorColorRight = getSensorColorRight()

    isBlueRangeR = blueRangeRightMin[0] <= valueSensorColorRight[0] <= blueRangeRightMax[0]
    isBlueRangeG = blueRangeRightMin[1] <= valueSensorColorRight[1] <= blueRangeRightMax[1]
    isBlueRangeB = blueRangeRightMin[2] <= valueSensorColorRight[2] <= blueRangeRightMax[2]

    return isBlueRangeR and isBlueRangeG and isBlueRangeB