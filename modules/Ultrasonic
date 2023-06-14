from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

sonic = UltrasonicSensor(Port.S1)

def distance():
    return sonic.distance()

def near_object():
    if distance() <= 110:
        return True
    else:
        return False
