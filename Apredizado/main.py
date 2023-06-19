#!/usr/bin/env pybricks-micropython
from Modules.movimentation import *

# Contadores
while True:
    if is_Red():
        First()
        #Contador_vermelho Atualiza para 1
    elif is_RedRight() and getContador_vermelho()==0:
        First_Red()
        
        
    elif is_RedRight() and getContador_vermelho()==1:
        First_Coleta()
        
    else:
        Follow_Line()
    