from modules.constants import *
from modules.motors import *
from modules.beep import *
from pybricks.tools import wait, StopWatch
try:
    data = open("data.txt", "r+")
except:
    data = open("data.txt", "x")
    data = open("data.txt", "r+")


def save_data():
    save = str(dic15) + "," + str(dic10) + "," + str(count) + "," + str(tube_count) + "," + str(tube15_position_initial) + "," + str(tube15_position_final) 
    data.write(save)


def load_data():
    global dic15, dic10, count
    data = open("data.txt", "r+")
    line = data.readline()
    line = line.split(",")
    dic15 = line[0]
    dic10 = line[1]
    count = line[2]


def reset():
    stop()
    global dic15, dic10, count, tube_count, tube15_position_initial, tube15_position_final
    print("reseted")
    dic10 = {'Lanchonete': False, 'Escola': False, 'Cinema': False}
    dic15 = {'Lanchonete': False, 'Escola': False, 'Cinema': False}
    # count = {"School": 0, "Movie": 0, "Lanchonete": 0, "Tube": 0}
    count = {}
    count["School"] = 0
    count["Movie"] = 0
    count["Lanchonete"] = 0
    count["Tube"] = 0
    
    print("Count: ", count)
    tube_count = 0
    tube15_position_initial = 0
    tube15_position_final = 0
    # wait(2000)
    while not len(ev3.buttons.pressed()) > 0:
        pass
    while len(ev3.buttons.pressed()) > 0:
        pass