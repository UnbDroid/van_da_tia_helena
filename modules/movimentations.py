from modules.colors import *
from modules.constants import *
from modules.motors import *


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
        move_distance_foward(90) 
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
        move_distance_foward(80)
        move_right(90)
        move_distance_foward(30)
        count["Tube"] += 1

def find_first_tube():
    first_pass_in_movie()
    first_pass_in_tube_area()

def adjust_blue():
    if is_blue_left():
        move_right(30)
        move_distance_foward(25)
        move_left(30)

def return_tube_area(place):
    if place  == "Lanchonete":
        move_distance_back(170)
        move_right(100)
        while not is_red_left():
            follow_line()
        lanchonete_to_tube_area()
        
    if place == "Escola":
        move_distance_back(160)
        move_left(100)
        move_distance_foward(120)
        while not is_red_right():
            follow_line()
        escola_to_tube_area()
    
    if place == "Cinema":
        move_distance_back(160)
        move_left(100)
        move_distance_foward(115)
        while not is_red_right():
            follow_line()
        cinema_to_tube_area()
        
        
        

def lanchonete_to_tube_area():
    if(is_red_left() and count["Tube"] != 0):
        move_distance_foward(80)
        move_left(90)
        move_distance_foward(30)
        count["Tube"] += 1 

def escola_to_tube_area():
    print('Escola indo pra area tube: ', count["Tube"])
    if(is_red_right() and count["Tube"] == 2): #2
        move_distance_foward(120)
        count["Tube"] += 1
    while not is_red_right():
        follow_line()
    print(count["Tube"]) ## teste
    if(is_red_right() and count["Tube"] == 3): #3
        move_distance_foward(80)
        move_right(90)
        move_distance_foward(30)



def cinema_to_tube_area():
    print('Cinema indo pra area tube: ', count["Tube"])
    if(is_red_right() and count["Tube"] == 3):
        move_distance_foward(120)
        count["Tube"] += 1
    while not is_red_right():
        follow_line()
    print(count["Tube"]) ## teste
    if(is_red_right() and count["Tube"] == 4):
        move_distance_foward(80)
        move_right(90)
        move_distance_foward(30)



