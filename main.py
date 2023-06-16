#!/usr/bin/env pybricks-micropython
from modules.movimentation import *
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port


ultrasonic = UltrasonicSensor(Port.S3)

while True:
    print(ultrasonic.distance())
    # start()
    # findFirstTube()
    # printColorRight()
    # printColorLeft()
    # print(isRed())
    # print('Direita', isRedRight())
    # print('Esquerda', isRedLeft())