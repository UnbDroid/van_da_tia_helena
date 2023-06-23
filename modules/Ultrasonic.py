from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port

sonic = UltrasonicSensor(Port.S3)

def distance():
    return sonic.distance()

def is_15_tube():
    if distance() <= 110:
        return True
    else:
        return False
