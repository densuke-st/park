#!/usr/bin/env python3
from tools.led import Led
from time import sleep
import atexit
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
atexit.register(GPIO.cleanup)

while True:
  # (1) LEDを制御する「モノ」を準備し、ledと名前をつけておく


  print("点けます")
  # (2) LEDにonを送り、電気信号を出す

  # (3) 1秒休む
  sleep(1)

  print("消します")
  # (4)  LEDにoffを送り、電気信号を止める

  # (5) また1秒休む
  sleep(1)


