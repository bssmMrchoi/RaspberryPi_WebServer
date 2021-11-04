import Adafruit_DHT
import time


class DHT11:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 18

    def getdht(self):
        hum, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        print(hum, temp)
        tm = time.localtime()
        return [temp, hum]
