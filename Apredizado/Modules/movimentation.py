from Modules.motores import *
from Modules.colors import *
from pybricks.media.ev3dev import SoundFile

Contador_vermelho=0

# Contadores --------------------------------------------------------

def getContador_vermelho():
    global Contador_vermelho
    return Contador_vermelho

def setContador_vermelho(value):
    global Contador_vermelho
    Contador_vermelho = value

# Moviment --------------------------------------------------------------

def Follow_Line():

    if is_BlackRight():
        Right(30)  
        
    elif is_BlackLeft():
        Left(30)    
    else:
        run()
    

def First():
    
    
    
    stop()
    
    dist(60)
    stop()
    
    Left(90)
    stop()
    
    dist(120)
    
        
def First_Red():
    
    setContador_vermelho(1)
    
    stop()
    dist(100)
    
    
def First_Coleta():
    
    stop()
    Right(90)
    dist(50)       
               
    
    


