#!/usr/bin/env pybricks-micropython
from Modules.movimentation import *

#TESTE DE COR ATUALIZAR DIÁRIO :))

# while True:
#     print("------------------")
#     print(color_left())
#     print(color_right())
#     print("------------------")
#     wait(500)


while True:
    if is_red():
        first()
        
    elif is_red_right() and get_contador_vermelho()==0:
        first_red()
        
        
    elif is_red_right() and get_contador_vermelho()==1:
        first_coleta()
    
    
    elif is_bluewhite():
        blue_line_coleta()
        
    else:
        follow_line()
    