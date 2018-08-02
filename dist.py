#!/usr/bin/env python3
from tools.led import Led
from tools.us import US
from time import sleep, time
import requests
import json
from RPi import GPIO
import atexit
atexit.register(GPIO.cleanup)

### 書き換えの必要な部分(ポート番号を書き換えてください)
led_port     = 0 # LEDとつながってるポート
us_trig_port = 0 # 距離センサー トリガーポート(trig)
us_echo_port = 0 # 距離センサー エコーポート(echo)
###

# 上記設定に合わせてLEDとUSの準備をする
led = Led(led_port)
us = US(us_trig_port,us_echo_port)

status = False # 近接の状態(False:離れた / True:近づいた)
led.off()
while True:
    dist = us.distance()  # 距離を計測して変数distに記録
    print("距離: " + str(dist))
    # 距離が10cm以上(dist >= 10) かつ 50cm以下(dist <= 50)、なおかつさっきまで離れていた
    if  dist >= 10 and dist <= 50 and status == False:
        # 近接状態を記録してLEDを点灯させる
        status = True
        led.on()
    # 近づいていた状態(status == True)のに離れた(dist > 50)
    elif status == True and dist > 50:
        # 近接状態を書き換えてLED消灯
        status = False
        led.off()
        
    sleep(1)
