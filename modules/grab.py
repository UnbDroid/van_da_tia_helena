from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time

grab = Motor(Port.C)

def close_grab():
    grab.run_time(-310, 4590)
    grab.hold()


def open_grab():
    grab.run(310) #Testar essa função depois
    time.sleep(4.5)#ver se conseguimos passar parametro que de um tempo relacionado ao tempo de fechamento ou se tempo constante é melhor
    grab.hold()