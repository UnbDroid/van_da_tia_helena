#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



#import time

#classDriveBase(left_motor, right_motor, wheel_diameter, axle_track)
#class Color

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Portas dos Motores Left and right
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)


# Touch sensor : meu botâo :D
botao = TouchSensor(Port.S1)

# Color sensor
line_sensorR = ColorSensor(Port.S3)
line_sensorL = ColorSensor(Port.S4)

# Ultrasonic Sensor
olhos_sensor = UltrasonicSensor(Port.S2) 

# Definindo Drivers Base para os motores (Whell diameter é o diametro da roda.) (Axle Track é as distâncias entre as duas rodas)
motores = DriveBase(left_motor, right_motor, wheel_diameter=41, axle_track=108)

# Definindo as cores que o sensor identifica
blackR = [5, 7, 5]
whiteR = [70, 80, 88] #    Direito
meioR = 44.5 # Definindo margem de erro

blackL = [8, 16, 8]
whiteL = [81, 100, 100 ] #    Esquerdo
meioL = 54 # Definindo margem de erro para a esquerda



redR = [59, 8, 5]  
redL = [68, 16,7]

# Definindo as médias para os sensores

media1 = 63.5 # Media entre sensores, mas é uma boa arrumar isso futuramente
media2 = 12
media3 = 6

cronometro = StopWatch()



ev3.speaker.beep()
motores.settings(straight_speed=200,turn_rate=120)
# Parametros:
#   straight_speed : Velocidade do robô 
#   turn_rate : Velocidade de giro do robô


apertou = False

# Definindo funções:

def VirarDireita():
    return (line_sensorR.rgb()[2] < meioR and line_sensorL.rgb()[2] >= meioL)

def VirarEsquerda():
    return (line_sensorL.rgb()[2] < meioL and line_sensorR.rgb()[2] >= meioR)


while True:
    if ((line_sensorR.rgb()[0] > 50 and line_sensorR.rgb()[1] <15)) and ((line_sensorL.rgb()[0] > 60 and line_sensorL.rgb()[1] < 25)):
        ev3.speaker.beep()
        motores.stop()
        break
        
    
    elif(line_sensorR.rgb()[2] >= meioR and line_sensorL.rgb()[2] >= meioL or line_sensorR.rgb()[2] <= meioR and line_sensorL.rgb()[2] <= meioL): #frente os dois
        motores.drive(180, 0) #arrumar o tamanho
        
    elif VirarDireita():
        motores.drive(40, 90) #DIREITA
        
    elif VirarEsquerda():
        motores.drive(40, -90) #ESQUERDA
        
        
    elif ((line_sensorR.rgb()[0] > 50 and line_sensorR.rgb()[1] <15)) or ((line_sensorL.rgb()[0] > 60 and line_sensorL.rgb()[1] < 25)):
        ev3.speaker.beep()
        motores.stop()
        wait(5000)
        ev3.speaker.beep()
        
    while (olhos_sensor.distance() <= 70):
        
        ev3.speaker.beep()
        motores.turn(90)
        motores.straight(150)
        
        motores.turn(-90)
        motores.straight(360)
        
        motores.turn(-70)
        while(line_sensorR.rgb()[2] >= meioR): 
           motores.drive(140, 0) 
        motores.turn(30)

cronometro.reset()





while cronometro.time() < 5000:
    if botao.pressed():
        apertou = True

if apertou == True:
    
    a  = True

    motores.turn(-85)
    motores.straight(140) 
    motores.turn(90)
    motores.straight(150) 
    while(a):
        ev3.speaker.beep(2)
   
                
        
else:  
    a  = True
   
    motores.turn(90)
    motores.straight(150) 
    motores.turn(-90)
    motores.straight(150) 
    while(a):
        ev3.speaker.beep(2)
   
                
        
        
    

    
        
        
       
       
        
  
