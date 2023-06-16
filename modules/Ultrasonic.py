from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase

sonic = UltrasonicSensor(Port.S3)

def distance():
    print(sonic.distance())
    return sonic.distance()

def near_object():
    if distance() <= 110:
        return True
    else:
        return False
