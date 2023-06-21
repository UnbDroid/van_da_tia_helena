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
    move_distance_back(100)
    while not is_black_right():
        move_foward(20)
        if is_blue_left():
            move_right(30)
            move_distance_foward(25)
            move_left(30)
        if near_object():
            stop()
            grab()
            grabbed = True
            wait(1000)
    stop()
    if(not grabbed):
        grab_next()
def grab(): # averiguar como escolher distancia
    move_left(90)
    move_distance_foward(50)  # calibrar depois
    Fechar()

def grab_next():
    move_distance_foward(70)  # averiguar como escolher distancia
    move_left(90)
    move_distance_foward(40)  # calibrar depois
    Fechar()

def follow_line():
    if(is_black_right()):
        move_right(20)
    elif(is_black_left()):
        move_left(20)
    else:
        move_foward(80)

def start():
    # leftGreen()
    # print("deu start")
    follow_line()
    if(is_red()):
        stop()
        wait(1000)
        move_distance_foward(70) 
        move_left(90)
        move_distance_foward(70) 
        count["School"] += 1

def first_pass_in_movie():
    if(is_red_right() and count["School"] == 1 and count["Movie"] == 0):
        stop()
        # print("passa_pelo movie")
        move_distance_foward(120)
        count["Movie"] += 1   

def first_pass_in_tube_area():
    if(is_red_right() and count["Movie"] == 1 and count["Tube"] == 0):
        stop()
        wait(2000)
        print("passa_pelo tubo")
        move_distance_foward(60)
        move_right(100)
        move_distance_foward(40)
        count["Tube"] += 1 

def ajust_blue_line():
    if(is_blue()):
        stop()
        move_distance_back(25)
        move_right(100)
        beggin_choosing()

def find_first_tube():
    # print("fidando first tube")
    first_pass_in_movie()
    first_pass_in_tube_area()
    ajust_blue_line()
