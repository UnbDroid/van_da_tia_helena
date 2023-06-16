from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
garra = Motor(Port.C)
motors = DriveBase(motorLeft, motorRight, wheel_diameter= 41, axle_track=108)
motors.settings(100, 270, 150) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro


def fechar():
    garra.run_until_stalled(180, then=Stop.COAST, duty_limit=None)
    garra.hold()


def Abrir():
    garra.speed(-180) #Testar essa função depois
    time.sleep(5)#ver se conseguimos passar parametro que de um tempo relacionado ao tempo de fechamento ou se tempo constante é melhor
    garra.hold()

def moveFoward(velocidade):
    motors.drive(velocidade, 0)

def moveBack(velocidade):
    motors.drive(-velocidade, 0)

def moveDistanceFoward(distance):
    motors.straight(distance)

def moveDistanceBack(distance):
    motors.straight(-distance)

def moveLeftTime(time):
    motors.drive_time(0, 80, time)

def moveRightTime(time):
    motors.drive_time(0, -80, time)

def moveLeft(angle):
    motors.turn(-angle)

def moveRight(angle):
    motors.turn(angle)

def stop():
    motors.stop()

