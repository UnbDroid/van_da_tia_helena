from modules.colors import *
from modules.motors import *
from pybricks.tools import wait, StopWatch

count = {}
count["School"] = 0
count["Movie"] = 0
count["Lanchonete"] = 0
count["Tube"] = 0

inicio = True

def followLine():
    if(isBlackRight()):
        moveRight(20)
    elif(isBlackLeft()):
        moveLeft(20)
    else:
        moveFoward(80)

def start():
    # leftGreen()
    followLine()
    if(isRed()):
        stop()
        wait(1000)
        moveDistanceFoward(70) 
        moveLeft(100)
        moveDistanceFoward(40) 
        count["School"] += 1

def firstPassInMovie():
    if(isRedRight() and count["School"] == 1 and count["Movie"] == 0):
        stop()
        wait(000)
        moveDistanceFoward(120)
        count["Movie"] += 1   

def firstPassInTubeArea():
    if(isRedRight() and count["Movie"] == 1 and count["Tube"] == 0):
        stop()
        wait(2000)
        moveDistanceFoward(60)
        moveRight(100)
        moveDistanceFoward(40)
        count["Tube"] += 1 

def ajustBlueLine():
    if(isBlue()):
        stop()
        wait(1000)
        moveDistanceBack(15)
        moveRight(100)

def findFirstTube():
    firstPassInMovie()
    firstPassInTubeArea()
    ajustBlueLine()

def leftGreen():
    if(getInicio() == True):
        moveDistanceFoward(100)
        setInicio(False)
        

def setInicio(value):
    global inicio
    inicio = value  

def getInicio():
    global inicio
    return inicio