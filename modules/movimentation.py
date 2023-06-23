from modules.colors import *
from modules.constants import *
from modules.motors import *
from pybricks.hubs import EV3Brick
from modules.tube import *

count = {}
count["School"] = 0
count["Movie"] = 0  # "Começar do vermelho área de coleta"
count["Lanchonete"] = 0
count["Tube"] = 0


def follow_line():
    if(is_black_right()):
        move_right(20)
    elif(is_black_left()):
        move_left(20)
    else:
        move_foward(80)

def start():
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
        move_distance_foward(120)
        count["Movie"] += 1   

def first_pass_in_tube_area():
    if(is_red_right() and count["Movie"] == 1 and count["Tube"] == 0):
        stop()
        wait(2000)
        
        move_distance_foward(60)
        move_right(90)
        move_distance_foward(30)
        count["Tube"] += 1 

def ajust_blue_line():
    if(is_blue()):
        stop()
        move_distance_back(25)
        move_right(100)
        beggin_choosing()

def find_first_tube():
    first_pass_in_movie()
    first_pass_in_tube_area()
    ajust_blue_line()

def adjust_blue():
    if is_blue_left():
        move_right(30)
        move_distance_foward(25)
        move_left(30)