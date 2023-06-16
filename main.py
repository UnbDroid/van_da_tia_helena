#!/usr/bin/env pybricks-micropython
<<<<<<< HEAD
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

sensor15 = UltrasonicSensor(Port.S1)
sensor10 = UltrasonicSensor(Port.S4)
motor = Motor(Port.A)

# while(True):
#     if (sensor15.distance() <= 100 and sensor10.distance() <= 100):
#         print("Tamanho 15")
#     elif(sensor10.distance() <= 100):
#         print("Tamanho 10")
#     else:
#         print("Nada")
# print('distancia 15 :', sensor15.distance() , 'distancia 10 :', sensor10.distance())
# Write your program here.
ev3.speaker.beep()


def fechar():
    while (Button.DOWN in ev3.buttons.pressed()):
        motor.run(180)
    motor.hold()


def Abrir():
    while Button.UP in ev3.buttons.pressed():
        motor.run(-180)
    motor.hold()


while True:
    fechar()
    Abrir()
=======
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
>>>>>>> felipe
