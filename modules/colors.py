from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


sensor_color_right = ColorSensor(Port.S2)
sensor_color_left = ColorSensor(Port.S1)


#Declarações de métodos

def get_sensor_color_right():
    return sensor_color_right.rgb()


def get_sensor_color_left():
    return sensor_color_left.rgb()


# WHITE
# ---------------------------------------------------------------------------------------------------------------------

white_range_left_min = [62, 65, 95]
white_range_left_max = [72, 75, 105]



def is_white_left():
    value_sensor_color_left = get_sensor_color_left()

    is_white_range_r = white_range_left_min[0] <= value_sensor_color_left[0] <= white_range_left_max[0]
    is_white_range_g = white_range_left_min[1] <= value_sensor_color_left[1] <= white_range_left_max[1]
    is_white_range_b = white_range_left_min[2] <= value_sensor_color_left[2] <= white_range_left_max[2]

    return is_white_range_r and is_white_range_g and is_white_range_b


white_range_right_min = [69, 69, 95]
white_range_right_max = [79, 79, 105]

def is_white_right():
    value_sensor_color_right = get_sensor_color_right()

    is_white_range_r = white_range_right_min[0] <= value_sensor_color_right[0] <= white_range_right_max[0]
    is_white_range_g = white_range_right_min[1] <= value_sensor_color_right[1] <= white_range_right_max[1]
    is_white_range_b = white_range_right_min[2] <= value_sensor_color_right[2] <= white_range_right_max[2]

    return is_white_range_r and is_white_range_g and is_white_range_b


def is_white():
    return is_white_right() and is_white_left()

# BLACK
# ---------------------------------------------------------------------------------------------------------------

black_range_left_min = [2, 4, 4]
black_range_left_max = [12, 14, 14]


def is_black_left():
    value_sensor_color_left = get_sensor_color_left()

    is_black_range_r = black_range_left_min[0] <= value_sensor_color_left[0] <= black_range_left_max[0]
    is_black_range_g = black_range_left_min[1] <= value_sensor_color_left[1] <= black_range_left_max[1]
    is_black_range_b = black_range_left_min[2] <= value_sensor_color_left[2] <= black_range_left_max[2]


    return is_black_range_r and is_black_range_g and is_black_range_b


black_range_right_min = [2, 4, 15]
black_range_right_max = [12, 14, 25]

def is_black_right():
    value_sensor_color_right = get_sensor_color_right()

    is_black_range_r = black_range_right_min[0] <= value_sensor_color_right[0] <= black_range_right_max[0]
    is_black_range_g = black_range_right_min[1] <= value_sensor_color_right[1] <= black_range_right_max[1]
    is_black_range_b = black_range_right_min[2] <= value_sensor_color_right[2] <= black_range_right_max[2]

    return is_black_range_r and is_black_range_g and is_black_range_b

def is_black():
    return is_black_right() and is_black_left()


# RED
# ---------------------------------------------------------------------------------------------------------------



red_range_right_min = [50, 4, 6]
red_range_right_max = [76, 17, 24]


def is_red_right():
    value_sensor_color_right = get_sensor_color_right()

    is_red_range_r = red_range_right_min[0] <= value_sensor_color_right[0] <= red_range_right_max[0]
    is_red_range_g = red_range_right_min[1] <= value_sensor_color_right[1] <= red_range_right_max[1]
    is_red_range_b = red_range_right_min[2] <= value_sensor_color_right[2] <= red_range_right_max[2]

   
    return is_red_range_r and is_red_range_g and is_red_range_b


#const
red_range_left_min = [55, 6, 6]
red_range_left_max = [75, 21, 30]



def is_red_left():
    value_sensor_color_left = get_sensor_color_left()

    is_red_range_r = red_range_left_min[0] <= value_sensor_color_left[0] <= red_range_left_max[0]
    is_red_range_g = red_range_left_min[1] <= value_sensor_color_left[1] <= red_range_left_max[1]
    is_red_range_b = red_range_left_min[2] <= value_sensor_color_left[2] <= red_range_left_max[2]

    

    return is_red_range_r and is_red_range_g and is_red_range_b


def is_red():
    return is_red_right() and is_red_left()

# BLUE
# ---------------------------------------------------------------------------------------------------------------

blue_range_left_min = [5, 28, 95]
blue_range_left_max = [15, 38, 105]

def is_blue_left():
    value_sensor_color_left = get_sensor_color_left()

    is_blue_range_r = blue_range_left_min[0] <= value_sensor_color_left[0] <= blue_range_left_max[0]
    is_blue_range_g = blue_range_left_min[1] <= value_sensor_color_left[1] <= blue_range_left_max[1]
    is_blue_range_b = blue_range_left_min[2] <= value_sensor_color_left[2] <= blue_range_left_max[2]

    return is_blue_range_r and is_blue_range_g and is_blue_range_b


blue_range_right_min = [7, 32, 95]
blue_range_right_max = [17, 42, 105]

def is_blue_right():
    value_sensor_color_right = get_sensor_color_right()

    is_blue_range_r = blue_range_right_min[0] <= value_sensor_color_right[0] <= blue_range_right_max[0]
    is_blue_range_g = blue_range_right_min[1] <= value_sensor_color_right[1] <= blue_range_right_max[1]
    is_blue_range_b = blue_range_right_min[2] <= value_sensor_color_right[2] <= blue_range_right_max[2]

    return is_blue_range_r and is_blue_range_g and is_blue_range_b


def is_blue():
    return is_blue_right() and is_blue_left()

# ---------------------------------------------------------------------------------------------------------------------

def print_color_right():
    return print('Direita: ', get_sensor_color_right())


def print_color_left():
    return print('Esquerda ', get_sensor_color_left())
