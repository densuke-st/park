#!/usr/bin/env python3 
from RPi import GPIO

class Led():
    """
    LEDの操作を行うクラス
    """

    port = 0 # 使用するGPIOポート番号

    def __init__(self,port):
        self.port = port        
        GPIO.setup(self.port, GPIO.OUT)
        self.off()

    def on(self):
        GPIO.output(self.port, True)
    
    def off(self):
        GPIO.output(self.port, False)

if __name__ == "__main__":
    from time import sleep
    GPIO.setmode(GPIO.BCM)
    l = led(21)
    while True:
        l.on()
        sleep(1)
        l.off()
        sleep(1)
