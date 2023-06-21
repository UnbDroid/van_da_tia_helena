from Modules.motores import *
from Modules.colors import *
from pybricks.media.ev3dev import SoundFile

Contador_vermelho=0

# Contadores --------------------------------------------------------

def get_contador_vermelho():
    global Contador_vermelho
    return Contador_vermelho

def set_contador_vermelho(value):
    global Contador_vermelho
    Contador_vermelho = value

# Moviment --------------------------------------------------------------

def follow_line():

    if is_black_right():
        right(30)  
        
    elif is_black_left():
        left(30)    
    else:
        run(120)
    

def first():
     
    stop(300)
    
    dist(60)
    stop(300)
    
    left(90)
    stop(300)
    
    dist(120)
    
        
def first_red():
    
    set_contador_vermelho(1)
    
    stop(300)
    dist(90)
    
    
def first_coleta():
    # Entrando no vermelho de coleta pela primeira vez !
    
    stop(300)
    dist(65)
    right(95)
    dist(45)
    
def blue_line_coleta():
    # Sempre que entrar na coleta irá fazer isso :))
    
    stop(300)
    dist(-25)
    right(94)
    print(is_white_left())
    
    while is_white_right():
        print("ENTREIIII!")
        run(-100)
    if is_black():
        stop(3000)
        #colocar ultrassom :))
    
    
    
               
    
    


