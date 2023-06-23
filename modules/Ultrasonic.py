from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from modules.movimentation import *

sonic = UltrasonicSensor(Port.S3)

def distance():
    return sonic.distance()

def is_15_tube():
    if distance() <= 110:
        return True
    else:
        return False
