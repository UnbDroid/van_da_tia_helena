from Modules.motores import *
from Modules.colors import *





def Follow_Line():

    if is_BlackRight():
        Right()  
        
    elif is_WhiteRight() and is_WhiteLeft():
        run()
         
    elif is_BlackLeft():
        Left()
    

def first():
    stop()
    
    dist(60)
    stop()
    
    Rodas.turn(-90)
    stop()
    
    dist(120)
        
        
    
    


