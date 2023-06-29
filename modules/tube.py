from modules.movimentations import *
from modules.constants import *
from modules.grab import *
from modules.ultrasonic import *
from pybricks.hubs import EV3Brick

from pybricks.tools import wait, StopWatch

clock = StopWatch()

ev3 = EV3Brick()

global tubo

global tube_count

global tube15_position_initial

global tube15_position_final

tube15_position_initial = 0
tube_count = 0
tube15_position_final = 0

def fetch_tube_area():
    global tubo, tube_count, tube15_position_initial, tube15_position_final
    if(is_blue()):
        stop()
        move_distance_back(23)
        move_right(90)
        grabbed = False
        move_distance_back(110)
        if(tube_count == 4 and tube15_position_initial != 4 and tube15_position_final != 4):
            grabbed = move_to_grab_final_10()
        elif(tube15_position_initial == 4):
            while not is_black_right():
                move_foward(80)
            grabbed = move_to_grab_next_tube()
        elif(tube15_position_final == 4):
            grabbed = move_to_grab_final_10()
        else: 
            grabbed = move_to_grab_tube()
        if(not grabbed):
            tubo = move_to_grab_next_tube()
        found_place(tubo)

def move_to_grab_final_10():
    global tubo
    move_distance_foward(50)
    move_left(85) # 90
    move_distance_foward(110)  
    close_grab()
    tubo = "tubo_10"
    move_distance_back(30)
    move_right(120)
    move_distance_back(30)
    return True


def move_to_grab_tube():
    global tubo, tube_count, tube15_position_initial

    clock.reset()
    clock.resume()
    TUBO_15 = False
    while clock.time() < 1200:
        move_foward(80)
        if is_15_tube():
            tubo = "tubo_15"
            ev3.speaker.beep(300)
            move_left(97)
            move_distance_foward(92)  
            close_grab()
            tube_count += 1
            tube15_position_initial += 1
            move_distance_back(30)
            move_right(120)
            move_distance_back(30)
            return True

def move_to_grab_next_tube():
    global tube_count, tube15_position_final

    clock.reset()
    clock.resume()
    TUBO_15 = False
    while clock.time() < 1180:
        move_foward(100)
        if is_15_tube():
            TUBO_15 = True
            move_left(97)
            move_distance_foward(90)  
            close_grab()
            tube_count += 1
            tube15_position_final += 1
            move_distance_back(30)
            move_left(120)
            move_distance_back(30)
            return "tubo_15"
    move_distance_back(70)
    move_left(85) # 90
    move_distance_foward(90)  
    close_grab()
    tube_count += 1
    move_distance_back(30)
    move_left(120)
    move_distance_back(30)  
    return "tubo_10"

def found_place(tubo):
    moved = False
    index = 0
    print('Pegou o tubo de: ', tubo)
    zero_dic15()
    zero_dic10()
    if tubo == "tubo_15":
        while index < len(dic15_keys) and not moved:
            place = dic15_keys[index]
            if not dic15[place]:
                moved = True
                dic15[place] = True
                leave_tube(place)
                print(place)
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
        while not is_red_right():
            follow_line()
        move_distance_foward(123)
        while not is_red_right():
            follow_line()
        move_distance_foward(60)
        move_right(90)
        move_distance_foward(170)
        open_grab()
        print("SOLTOU")
        
    elif place == "Cinema":
        print("indo pro cinema")
        move_left(80)
        move_distance_foward(42)
        while not is_red_left():
            follow_line()
        move_distance_foward(60)
        move_left(90)
        move_distance_foward(170)
        open_grab()
        print("SOLTOU")
        

def zero_dic15():
    if(dic15["Lanchonete"] and dic15["Cinema"] and dic15["Escola"]):
        dic15["Lanchonete"] = False
        dic15["Cinema"] = False
        dic15["Escola"] = False

def zero_dic10():
    if(dic10["Lanchonete"] and dic10["Cinema"] and dic10["Escola"]):
        dic10["Lanchonete"] = False
        dic10["Cinema"] = False
        dic10["Escola"] = False