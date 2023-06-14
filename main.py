#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Conexoes 
ev3 = EV3Brick()

# Conexões Motores:
LeftMotor = Motor(Port.A)
RightMotor = Motor(Port.B)
Motores = DriveBase(LeftMotor,RightMotor,41, 113)

# Sensores: 
LeftSensor = ColorSensor(Port.S1)
RightSensor = ColorSensor(Port.S4)

#       Algumas anotações:
# Left Sensor : Branco = (36, 33, 94) Preto = (6, 6, 13) Vermelho = (31, 4, 5)

# Right Sensor: Branco = (24, 29, 31) Preto = (3, 3, 1)  Vermelho = (23, 3, 0)

# Funções :

def RunWhite():
    while LeftSensor.rgb()[2] > 89 and LeftSensor.rgb()[2] <100:
        Motores.drive(200,0)
        
        
def LeftRed():
    while LeftSensor.rgb()[0] > 25 and LeftSensor.rgb()[0] < 39:
        Motores.drive(200,0)
        if LeftSensor.rgb()[2] > 8 and LeftSensor.rgb()[2] < 20:
            Motores.drive(150,90)

# Alguns Testes.
ev3.speaker.beep()
while True:
    if (LeftSensor.rgb()[2] > 89 ) or (LeftSensor.rgb()[0] > 25 ):
        Motores.drive(200,0)
        
    while LeftSensor.rgb()[2] > 8 and LeftSensor.rgb()[2] < 20:
            Motores.drive(150,-200)
            
    while RightSensor.rgb()[0] > 0 and RightSensor.rgb()[2] < 10:
            Motores.drive(150,200)
    
    
    
    
    