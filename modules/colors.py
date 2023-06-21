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

white_range_left_r = [31, 32, 33, 34, 35, 36, 37]
white_range_left_g = [28, 29, 30 ,31, 32, 33, 34, 35, 36]
white_range_left_b = [90, 89 ,88, 87, 86, 85, 84]


def is_white_left():
    value_sensor_color_left = get_sensor_color_left()

    is_white_range_r = value_sensor_color_left[0] in white_range_left_r
    is_white_range_g = value_sensor_color_left[1] in white_range_left_g
    is_white_range_b = value_sensor_color_left[2] in white_range_left_b

    return is_white_range_r and is_white_range_g and is_white_range_b


white_range_right_min = [35, 30, 95]
white_range_right_max = [45, 40, 105]

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

black_range_left_r = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]
black_range_left_g = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]
black_range_left_b = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13]


def is_black_left():
    value_sensor_color_left = get_sensor_color_left()

    is_black_range_r = value_sensor_color_left[0] in black_range_left_r
    is_black_range_g = value_sensor_color_left[1] in black_range_left_g
    is_black_range_b = value_sensor_color_left[2] in black_range_left_b

    return is_black_range_r and is_black_range_g and is_black_range_b


black_range_right_min = [1, 2, 3]
black_range_right_max = [12, 20, 12]

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

# red_range_right_r = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
# red_range_right_g = [1, 2, 3, 4, 5, 6, 7]
# red_range_right_b = [0, 1, 2, 3, 4]

red_range_right_r = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
red_range_right_g = [1, 2, 3, 4, 5, 6, 7]
red_range_right_b = [7, 8, 9, 10, 11, 12, 13, 14]


def is_red_right():
    value_sensor_color_right = get_sensor_color_right()

    is_red_range_r = value_sensor_color_right[0] in red_range_right_r
    is_red_range_g = value_sensor_color_right[1] in red_range_right_g
    is_red_range_b = value_sensor_color_right[2] in red_range_right_b

    # print('R', is_red_range_r)
    # print('G', is_red_range_g)
    # print('B', is_red_range_b)

    return is_red_range_r and is_red_range_g and is_red_range_b



red_range_left_min = [25, 1, 2]
red_range_left_max = [40, 10, 12]

def is_red_left():
    value_sensor_color_left = get_sensor_color_left()

    is_red_range_r = red_range_left_min[0] <= value_sensor_color_left[0] <= red_range_left_max[0]
    is_red_range_g = red_range_left_min[1] <= value_sensor_color_left[1] <= red_range_left_max[1]
    is_red_range_b = red_range_left_min[2] <= value_sensor_color_left[2] <= red_range_left_max[2]

    # print('R', is_red_range_r)
    # print('G', is_red_range_g)
    # print('B', is_red_range_b)

    return is_red_range_r and is_red_range_g and is_red_range_b


def is_red():
    return is_red_right() and is_red_left()

# BLUE
# ---------------------------------------------------------------------------------------------------------------

blue_range_left_min = [3, 11, 55]
blue_range_left_max = [8, 20, 65]

def is_blue_left():
    value_sensor_color_left = get_sensor_color_left()

    is_blue_range_r = blue_range_left_min[0] <= value_sensor_color_left[0] <= blue_range_left_max[0]
    is_blue_range_g = blue_range_left_min[1] <= value_sensor_color_left[1] <= blue_range_left_max[1]
    is_blue_range_b = blue_range_left_min[2] <= value_sensor_color_left[2] <= blue_range_left_max[2]

    return is_blue_range_r and is_blue_range_g and is_blue_range_b


blue_range_right_min = [1, 12, 78]
blue_range_right_max = [10, 20, 85]

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
