from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from modules.motors import *
from modules.colors import *
from modules.sensorUltrasonic import *

def beggin_choosing():
    moveFoward(40)
    while not through_line():

