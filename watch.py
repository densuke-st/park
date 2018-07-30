#!/usr/bin/env python3
from tools.led import Led
from tools.us import US
from time import sleep
import requests
import json
from RPi import GPIO

### 書き換えの必要な部分
led_port = 26 # LEDとつながってるポート
us_trig_port = 23 # 距離センサー トリガーポート(trig)
us_echo_port = 24 # 距離センサー エコーポート(echo)

park_no = 1  # 駐車場番号(パネルの番号)
###


led = Led(led_port)
us = US(us_trig_port,us_echo_port)


import atexit
atexit.register(GPIO.cleanup)

URL = "http://10.0.16.254:8080/v1/update"
def post(status):
    data = {
        "parkno": park_no,
        "status": status
    }
    print(data)
    requests.post(URL, json=data)

from time import time

status = False
led.off()
while True:
    dist = us.distance()
    print("距離: " + str(dist))
    if  dist >= 10 and dist <= 50 and status == False:
        post(True)
        status = True
        led.on()
    elif status == True and dist > 50:
        post(False)
        status = False
        led.off()
        
    sleep(1)
