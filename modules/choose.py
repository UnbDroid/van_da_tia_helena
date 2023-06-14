from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from modules.motors import *
from modules.colors import *
from modules.Ultrasonic import *


def beggin_choosing():
    moveFoward(40)
    while not through_line():
        if near_object():
            #fazer função de fechar a garra
            pass
    stop()
    grab_next()

def grab_next():
    moveDistanceFoward(500) #averiguar como escolher distancia
    turnAngle(-90)
    moveDistanceFoward(100) #calibrar depois
    fechar()

