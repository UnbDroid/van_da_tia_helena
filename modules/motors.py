from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)

motors = DriveBase(motorLeft, motorRight, wheel_diameter= 41, axle_track=108)
motors.settings(100, 270, 150) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro


def moveFoward(velocidade):
    motors.drive(velocidade, 0)

def moveBack(velocidade):
    motors.drive(-velocidade, 0)

def moveDistanceFoward(distance):
    motors.straight(distance)

def moveDistanceBack(distance):
    motors.straight(-distance)

def turnAngle(angle):
    motors.turn(angle)

def stop():
    motors.stop()

