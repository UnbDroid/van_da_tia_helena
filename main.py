#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.motors import *

while True:
    moveFoward(100)
    if isBlueRight():
        moveStop()
        break