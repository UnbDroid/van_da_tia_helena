from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)

Rodas = DriveBase(motorLeft, motorRight, wheel_diameter=41, axle_track=106.5)


# def Standard():
#     Rodas.settings(straight_speed=100,straight_acceleration=100) 

def dist(i):
    Rodas.straight(i)
    
def run():
    Rodas.drive(150,0)

def stop():
    Rodas.stop()
    wait(300)
    
def Left(value):
    Rodas.turn(-value)
   
    
def Right(value):
    Rodas.turn(value)
    
    
