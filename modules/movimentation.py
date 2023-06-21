from modules.colors import *
from modules.motors import *
from modules.Ultrasonic import *
from pybricks.tools import wait, StopWatch

count = {}
count["School"] = 0
count["Movie"] = 0
count["Lanchonete"] = 0
count["Tube"] = 0

inicio = True


def beggin_choosing():
    # print("begginado")
    grabbed = False
    moveDistanceBack(100)
    while not isBlackRight():
        moveFoward(20)
        if isBlueLeft():
            moveRigth(10)
        if near_object():
            stop()
            grab()
            grabbed = True
            wait(1000)
    stop()
    if(not grabbed):
        grab_next()
def grab(): # averiguar como escolher distancia
    moveLeft(90)
    moveDistanceFoward(20)  # calibrar depois
    fechar()

def grab_next():
    moveDistanceFoward(50)  # averiguar como escolher distancia
    moveLeft(90)
    moveDistanceFoward(20)  # calibrar depois
    fechar()

def followLine():
    if(isBlackRight()):
        moveRight(20)
    elif(isBlackLeft()):
        moveLeft(20)
    else:
        moveFoward(80)

def start():
    # leftGreen()
    # print("deu start")
    followLine()
    if(isRed()):
        stop()
        wait(1000)
        moveDistanceFoward(70) 
        moveLeft(90)
        moveDistanceFoward(70) 
        count["School"] += 1

def firstPassInMovie():
    if(isRedRight() and count["School"] == 1 and count["Movie"] == 0):
        stop()
        # print("passa_pelo movie")
        moveDistanceFoward(120)
        count["Movie"] += 1   

def firstPassInTubeArea():
    if(isRedRight() and count["Movie"] == 1 and count["Tube"] == 0):
        stop()
        wait(2000)
        print("passa_pelo tubo")
        moveDistanceFoward(60)
        moveRight(100)
        moveDistanceFoward(40)
        count["Tube"] += 1 

def ajustBlueLine():
    if(isBlue()):
        stop()
        # print("ajustou")
        moveDistanceBack(25)
        moveRight(100)
        beggin_choosing()

def findFirstTube():
    # print("fidando first tube")
    firstPassInMovie()
    firstPassInTubeArea()
    ajustBlueLine()



        

