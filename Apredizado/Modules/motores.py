from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)

Rodas = DriveBase(motorLeft, motorRight, wheel_diameter=41, axle_track=106.5)




def dist(i):
    Rodas.straight(i)
    
def run(velocidade):
    Rodas.drive(velocidade,0)
    
def back(velocidade):
    Rodas.drive(-velocidade,0)
    
def stop(tempo):
    Rodas.stop()
    wait(tempo)
    
def left(value):
    Rodas.turn(-value)
   
    
def right(value):
    Rodas.turn(value)
    
    
