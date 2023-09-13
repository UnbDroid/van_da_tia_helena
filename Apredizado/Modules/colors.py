# Importações : 

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from Modules.constantes import *

sensorColorRight = ColorSensor(Port.S2)
sensorColorLeft = ColorSensor(Port.S1)

# Definindo RGB
# ---------------------------------------------------------------------------------------------------------------------------------------#


def color_right():
    return sensorColorRight.rgb()


def color_left():
    return sensorColorLeft.rgb()
    

# Black 
# ---------------------------------------------------------------------------------------------------------------------------------------#


def is_black_right():
    
    
    isBlackR = BLACK_RANGE_RIGHT_MIN[0] <= color_right()[0] <= BLACK_RANGE_RIGHT_MAX[0]
    isBlackG = BLACK_RANGE_RIGHT_MIN[1] <= color_right()[1] <= BLACK_RANGE_RIGHT_MAX[1]
    isBlackB = BLACK_RANGE_RIGHT_MIN[2] <= color_right()[2] <= BLACK_RANGE_RIGHT_MAX[2]
    
    return isBlackR and isBlackG and isBlackB

def is_black_left():
    isBlackR = BLACK_RANGE_LEFT_MIN[0] <= color_left()[0] <= BLACK_RANGE_LEFT_MAX[0]
    isBlackG = BLACK_RANGE_LEFT_MIN[1] <= color_left()[1] <= BLACK_RANGE_LEFT_MAX[1]
    isBlackB = BLACK_RANGE_LEFT_MIN[2] <= color_left()[2] <= BLACK_RANGE_LEFT_MAX[2]
    
    return isBlackR and isBlackG and isBlackB

def is_black():
    return is_black_right() and is_black_left()


# White
# ---------------------------------------------------------------------------------------------------------------------------------------#


def is_white_right():
    
    
    isWhiteR = WHITE_RANGE_RIGHT_MIN[0] <= color_right()[0] <= WHITE_RANGE_RIGHT_MAX[0]
    isWhiteG = WHITE_RANGE_RIGHT_MIN[1] <= color_right()[1] <= WHITE_RANGE_RIGHT_MAX[1]
    isWhiteB = WHITE_RANGE_RIGHT_MIN[2] <= color_right()[2] <= WHITE_RANGE_RIGHT_MAX[2]
    
    
    return isWhiteR and isWhiteG and isWhiteB

def is_white_left():
    isWhiteR = WHITE_RANGE_LEFT_MIN[0] <= color_left()[0] <= WHITE_RANGE_LEFT_MAX[0]
    isWhiteG = WHITE_RANGE_LEFT_MIN[1] <= color_left()[1] <= WHITE_RANGE_LEFT_MAX[1]
    isWhiteB = WHITE_RANGE_LEFT_MIN[2] <= color_left()[2] <= WHITE_RANGE_LEFT_MAX[2]
    
    return isWhiteR and isWhiteG and isWhiteB

def is_white():
    return is_white_right() and is_white_left()


# Red
# ------------------------------------------------------------------------------------------------------------------------ #

def is_red_right():
    
    isRedR = RED_RANGE_RIGHT_MIN[0] <= color_right()[0] <= RED_RANGE_RIGHT_MAX[0]
    isRedG = RED_RANGE_RIGHT_MIN[1] <= color_right()[1] <= RED_RANGE_RIGHT_MAX[1]
    isRedB = RED_RANGE_RIGHT_MIN[2] <= color_right()[2] <= RED_RANGE_RIGHT_MAX[2]
    
    return isRedR and isRedG and isRedB

def is_red_left():
    
    isRedR = RED_RANGE_LEFT_MIN[0] <= color_left()[0] <= RED_RANGE_LEFT_MAX[0]
    isRedG = RED_RANGE_LEFT_MIN[1] <= color_left()[1] <= RED_RANGE_LEFT_MAX[1]
    isRedB = RED_RANGE_LEFT_MIN[2] <= color_left()[2] <= RED_RANGE_LEFT_MAX[2]
    
    return isRedR and isRedG and isRedB

def is_red():
    return is_red_right() and is_red_left()

# Blue
# ------------------------------------------------------------------------------------------------------------------------ #

def is_blue_right():

    isBlueR = BLUE_RANGE_RIGHT_MIN[0] <= color_right()[0] <= BLUE_RANGE_RIGHT_MAX[0]
    isBlueG = BLUE_RANGE_RIGHT_MIN[1] <= color_right()[1] <= BLUE_RANGE_RIGHT_MAX[1]
    isBlueB = BLUE_RANGE_RIGHT_MIN[2] <= color_right()[2] <= BLUE_RANGE_RIGHT_MAX[2]
    
    return isBlueR and isBlueG and isBlueB

def is_blue_left():

    isBlueR = BLUE_RANGE_LEFT_MIN[0] <= color_left()[0] <= BLUE_RANGE_LEFT_MAX[0]
    isBlueG = BLUE_RANGE_LEFT_MIN[1] <= color_left()[1] <= BLUE_RANGE_LEFT_MAX[1]
    isBlueB = BLUE_RANGE_LEFT_MIN[2] <= color_left()[2] <= BLUE_RANGE_LEFT_MAX[2]
    
    return isBlueR and isBlueG and isBlueB

def is_blue():
    return is_blue_right() and is_blue_left()

# BLUE AND WHITE

def is_bluewhite_right():
    
    isBlueR = BLUEWHITE_RANGE_RIGHT_MIN[0] <= color_right()[0] <= BLUEWHITE_RANGE_RIGHT_MAX[0]
    isBlueG = BLUEWHITE_RANGE_RIGHT_MIN[1] <= color_right()[1] <= BLUEWHITE_RANGE_RIGHT_MAX[1]
    isBlueB = BLUEWHITE_RANGE_RIGHT_MIN[2] <= color_right()[2] <= BLUEWHITE_RANGE_RIGHT_MAX[2]
    
    return isBlueR and isBlueG and isBlueB

def is_bluewhite_left():
    
    isBlueR = BLUEWHITE_RANGE_LEFT_MIN[0] <= color_left()[0] <= BLUEWHITE_RANGE_LEFT_MAX[0]
    isBlueG = BLUEWHITE_RANGE_LEFT_MIN[1] <= color_left()[1] <= BLUEWHITE_RANGE_LEFT_MAX[1]
    isBlueB = BLUEWHITE_RANGE_LEFT_MIN[2] <= color_left()[2] <= BLUEWHITE_RANGE_LEFT_MAX[2]
    
    return isBlueR and isBlueG and isBlueB

def is_bluewhite():
    return is_bluewhite_right() and is_bluewhite_left()
    


    


    

