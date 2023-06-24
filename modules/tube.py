from modules.movimentations import *
from modules.constants import *
from modules.grab import *
from modules.ultrasonic import *
from pybricks.hubs import EV3Brick

from pybricks.tools import wait, StopWatch

clock = StopWatch()

ev3 = EV3Brick()

def fetch_tube_area():
    if(is_blue()):
        stop()
        move_distance_back(25)
        move_right(100)
        grabbed = False
        move_distance_back(100)
        while not is_black_right():
            move_foward(20)
            adjust_blue()
            if is_15_tube():
            # Count tubo 15
                stop()
                ev3.speaker.beep(300)
                tubo = "tubo_15"
                grabbed = move_to_grab_tube()
                break
        if(not grabbed):
            tubo = move_to_grab_next_tube()
        found_place(tubo)

def move_to_grab_tube():
    move_left(90)
    move_distance_foward(90)
    close_grab()
    move_distance_back(30)
    move_right(120)
    move_distance_foward(40)
    return True

def move_to_grab_next_tube():
    clock.reset()
    clock.resume()
    TUBO_15 = False
    count_tubo_15 = 0
    count_tubo_10 = 0
    while clock.time() < 1181:
        move_foward(100)
        if is_15_tube():
            count_tubo_15 += 1
            TUBO_15 = True
            move_left(90)
            move_distance_foward(85)  # calibrar depois
            close_grab()
            move_distance_back(30)
            move_left(120)
            move_distance_back(30)
            return "tubo_15"
    move_distance_foward(-20)
    move_left(90)
    move_distance_foward(85)  # calibrar depois
    close_grab()
    count_tubo_10 += 1
    close_grab()
    move_distance_back(30)
    move_left(120)
    move_distance_back(30)
    return "tubo_10"

def found_place(tubo):
    moved = False
    index = 0
    if tubo == "tubo_15":
        while index < len(dic15_keys) and not moved:
            place = dic15_keys[index]
            if not dic15[place]:
                moved = True
                dic15[place] = True
                leave_tube(place)
                print("movou")
                return_tube_area(place)
            index +=1
    if tubo == "tubo_10":
        while index < len(dic10_keys) and not moved:
            place = dic10_keys[index]
            if not dic10[place]:
                dic10[place] = True
                moved = True
                leave_tube(place)
                print("mouvou")
                return_tube_area(place)
            index +=1

def leave_tube(place):
    ev3.speaker.beep(120)
    print(place)
    while not is_red():
        if is_black():
            move_right(40)
        follow_line()
    stop()
    move_distance_foward(70)
    if place == "Lanchonete":
        move_right(80)
        move_distance_foward(42)
        while not is_red_right():
            follow_line()
        move_distance_foward(60)
        move_right(90)
        move_distance_foward(150)
        open_grab()
        print("SOLTOU")
    elif place == "Escola":
        move_right(80)
        move_distance_foward(42)
        while not is_red_left():
            if is_red_right():
                move_distance_foward(120)
            follow_line()
        move_distance_foward(60)
        move_right(90)
        move_distance_foward(170)
        open_grab()
        print("SOLTOU")


