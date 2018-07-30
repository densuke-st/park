#!/usr/bin/env python3
from tools.led import Led
from time import sleep
from RPi import GPIO
import atexit

GPIO.setmode(GPIO.BCM)
atexit.register(GPIO.cleanup)

# (1) LEDを制御する「モノ」を準備し、ledと名前をつけておく
led = Led(26) 

print("点けます")
# (2) LEDにonを送り、電気信号を出す
led.on()
# (3) 1秒休む
sleep(1)

print("消します")
# (4)  LEDにoffを送り、電気信号を止める
led.off()

