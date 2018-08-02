from tools.led import Led
from tools.us import US
from RPi import GPIO
from time import sleep

import atexit
atexit.register(GPIO.cleanup)

def execfile(filename):
    exec(open(filename).read())

