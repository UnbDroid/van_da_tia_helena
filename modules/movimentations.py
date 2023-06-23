from modules.colors import *
from modules.constants import *
from modules.motors import *
from pybricks.hubs import EV3Brick
from modules.grab import *
from modules.ultrasonic import *
from pybricks.tools import wait, StopWatch


relogio = StopWatch()

ev3 = EV3Brick()

def comeback(place):
    print("comebacko")
    if place  == "Lanchonete":
        move_left(180)
        while not is_red():
            follow_line()
        stop()
        move_distance_foward(20)
        move_left(90)
        move_distance_foward(20)
        while not is_red_left():
            follow_line()
        stop()
    

def found_place(tubo):
    moved = False
    index = 0
    if tubo == "tubo_15":
        while index < len(dic15_keys) and not moved:
            place = dic15_keys[index]
            if not dic15[place]:
                moved = True
                dic15[place] = True
                move_to(place)
                print("movou")
                comeback(place)
            index +=1
    if tubo == "tubo_10":
        while index < len(dic10_keys) and not moved:
            place = dic10_keys[index]
            if not dic10[place]:
                dic10[place] = True
                moved = True
                move_to(place)
                print("mouvou")
                comeback(place)
            index +=1

def beggin_choosing():
    grabbed = False
    move_distance_back(100)
    while not is_black():
        move_foward(20)
        adjust_blue()
        if is_15_tube():
            # Count tubo 15
            stop()
            ev3.speaker.beep(300)
            tubo = "tubo_15"
            grabbed = grab()
            break
    if(not grabbed):
        tubo = grab_next()
    found_place(tubo)
        

def adjust_blue():
    if is_blue_left():
        move_right(30)
        move_distance_foward(25)
        move_left(30)
def grab(): # averiguar como escolher distancia
    move_left(90)
    move_distance_foward(90)
      # calibrar depois
    close_grab()
    move_distance_back(30)
    move_right(120)
    move_distance_foward(40)
    return True

def grab_next():
    relogio.reset()
    relogio.resume()
    TUBO_15 = False
    count_tubo_15 = 0
    count_tubo_10 = 0
    while relogio.time() < 1181:
        move_foward(100)
        if is_15_tube():
            count_tubo_15 += 1
            TUBO_15 = True
            move_left(90)
            move_distance_foward(85)  # calibrar depois
            close_grab()
            stop()
            return "tubo_15"
    move_distance_foward(-20)
    move_left(90)
    move_distance_foward(85)  # calibrar depois
    close_grab()
    stop()
    wait(2000)
    count_tubo_10 += 1
    close_grab()
    stop()
    return "tubo_10"
# from modules.tube import beggin_choosing
from pybricks.tools import wait

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
        move_right(110)
        beggin_choosing()

def find_first_tube():
    first_pass_in_movie()
    first_pass_in_tube_area()
    ajust_blue_line()



################################################################################################################


relogio = StopWatch()

ev3 = EV3Brick()


def move_to(place):
    ev3.speaker.beep(120)
    print(place)
    while not is_red():
        follow_line()
    stop()
    move_distance_foward(50)
    if place == "Lanchonete":
        move_right(90)
        move_distance_foward(30)
        while not is_red_right():
            follow_line()
        move_distance_foward(60)
        move_right(90)
        move_distance_foward(90)
        open_grab()
        print("SOLTOU")
        comeback(place)
    else:
        print("else")


