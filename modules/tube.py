from modules.grab import *
from modules.constants import *
from modules.ultrasonic import *
from pybricks.tools import wait, StopWatch
from modules.movimentation import *


relogio = StopWatch()

ev3 = EV3Brick()

def comeback(place):
    pass

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
        move_distance_foward(40)
        move_right(90)
        move_distance_foward(80)
        open_grab()
    else:
        pass
    comeback(place)

def found_place(tubo):
    if tubo == "tubo_15":
        for place in dic15_keys:
            if not dic15[place]:
                dic15[place] = True
                move_to(place)
                break
    if tubo == "tubo_10":
        for place in dic10_keys:
            if not dic10[place]:
                dic10[place] = True
                move_to(place)
                break

def beggin_choosing():
    grabbed = False
    move_distance_back(100)
    while not is_black_left():
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