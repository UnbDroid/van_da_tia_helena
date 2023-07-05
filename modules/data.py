from modules.constants import *
from pybricks.tools import wait, StopWatch
try:
    data = open("data.txt", "r+")
except:
    data = open("data.txt", "x")
    data = open("data.txt", "r+")


def save_data():
    save = str(dic15) + "," +  str(dic10) + ","  + str(count)
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
    global dic15, dic10, count
    print("reseted")
    dic10 = {'Lanchonete': False, 'Escola': False, 'Cinema': False}
    dic15 = {'Lanchonete': False, 'Escola': False, 'Cinema': False}
    count = {"School": 0, "Movie": 0, "Lanchonete": 0, "Tube" :0}
    wait(2000)