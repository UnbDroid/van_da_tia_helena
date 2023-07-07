from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)

motors = DriveBase(motorLeft, motorRight, wheel_diameter= 41, axle_track=108.2)
motors.settings(150, 270, 250) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro


def move_foward(velocidade):
    motors.drive(velocidade, 0)

def move_back(velocidade):
    motors.drive(-velocidade, 0)

def move_distance_foward(distance):
    motors.straight(distance)

def move_distance_back(distance):
    motors.straight(-distance)

def move_left_time(time):
    motors.drive_time(0, 80, time)

def move_right_time(time):
    motors.drive_time(0, -80, time)

def move_left(angle):
    motors.turn(-angle)

def move_right(angle):
    motors.turn(angle)

def stop():
    motors.stop()

