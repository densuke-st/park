#!/usr/bin/env python3 

from RPi import GPIO
from time import sleep, time

class US():

    port_trig = 0
    port_echo = 0

    def __init__(self, trig, echo):
        self.port_trig = trig
        self.port_echo = echo
        GPIO.setup(self.port_trig, GPIO.OUT)
        GPIO.setup(self.port_echo, GPIO.IN)
    
    def distance(self):

        # トリガーピンに信号を送る
        GPIO.output(self.port_trig, True)
        sleep(0.00001)
        GPIO.output(self.port_trig, False)

        # エコーポートが上がるまで時間を取得
        start = time()
        stop = 0
        while GPIO.input(self.port_echo) == 0:
            start = time()
        
        # エコーポートが上がっている間時間を取得
        while GPIO.input(self.port_echo) == 1:
            stop = time()
        
        # 差し引きで上がっていた時間を取得
        e = stop - start
        # 音速(340m/s)で往復時間を計測して半分にする
        dist = e * 34000 / 2
        return dist

if __name__ == "__main__":
    import atexit
    atexit.register(GPIO.cleanup)
    GPIO.setmode(GPIO.BCM)
    us = US(20,16)
    while True:
        d = us.distance()
        print("距離: " + str(d))
        sleep(1)
