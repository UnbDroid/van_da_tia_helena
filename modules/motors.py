from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
garra = Motor(Port.C)
motors = DriveBase(motorLeft, motorRight, wheel_diameter= 41, axle_track=106.5)
motors.settings(100, 270, 150) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro


def Fechar():
    garra.run(-300)
    time.sleep(5)
    garra.stop()
    garra.hold()


def Abrir():
    garra.run(300) #Testar essa função depois
    time.sleep(5)#ver se conseguimos passar parametro que de um tempo relacionado ao tempo de fechamento ou se tempo constante é melhor
    garra.hold()

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

