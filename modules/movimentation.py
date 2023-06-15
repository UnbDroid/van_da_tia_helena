from modules.colors import *
from modules.motors import *
from pybricks.tools import wait, StopWatch

count = {}
count["School"] = 0
count["Movie"] = 0
count["Lanchonete"] = 0
count["Tube"] = 0

def followLine():
    if(isBlackRight()):
        moveRightTime(400)
    elif(isBlackLeft()):
        moveLeftTime(400)
    elif(isBlack()):
        stop()
        wait(2000)
        moveLeft(20)
    else:
        moveFoward(80)

def start():
    followLine()
    if(isRed()):
        stop()
        wait(1000)
        moveLeft(140)
        moveDistanceFoward(1000) 
        moveLeft(140) 
        count["School"] += 1

def firstPassInMovie():
    if(isRedRight() and count["Movie"] == 0):
        stop()
        wait(2000)
        moveDistanceFoward(200)
        count["Movie"] += 1   

def firstPassInTubeArea():
    if(isRedRight() and count["Tube"] == 0 and count["Movie"] == 1):
        stop()
        wait(2000)
        moveRight(100)
        count["Tube"] += 1 

def ajustBlueLine():
    if(isBlue()):
        stop()
        wait(5000)

def findFirstTube():
    firstPassInMovie()
    firstPassInTubeArea()
    ajustBlueLine()
        
    