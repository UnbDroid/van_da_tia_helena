#!/usr/bin/env pybricks-micropython
from modules.movimentation import *

# sensor15 = UltrasonicSensor(Port.S1)
# sensor10 = UltrasonicSensor(Port.S4)
# motor = Motor(Port.A)



# while True:
#     print("--------------")
#     print(print_color_right())
#     print(print_color_left())
#     print("--------------")
#     wait(500)
    




# while(True):
#     if (sensor15.distance() <= 100 and sensor10.distance() <= 100):
#         print("Tamanho 15")
#     elif(sensor10.distance() <= 100):
#         print("Tamanho 10")
#     else:
#         print("Nada")
# print('distancia 15 :', sensor15.distance() , 'distancia 10 :', sensor10.distance())
# Write your program here.
# ev3.speaker.beep()


# def fechar():
#     while (Button.DOWN in ev3.buttons.pressed()):
#         motor.run(180)
#     motor.hold()


# def Abrir():
#     while Button.UP in ev3.buttons.pressed():
#         motor.run(-180)
#     motor.hold()

while True:
   start()
   find_first_tube()
    
# DEPOIS DA LINHA PRETA INCREMENTAR !!!!

print(count_tubo_15)
print(count_tubo_10)
    
