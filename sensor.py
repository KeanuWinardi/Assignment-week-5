import time
import Adafruit_DHT

sens = Adafruit_DHT.DHT11
gpio = 4

while True:
    humi, temp = Adafruit_DHT.read_retry(sens, gpio)
    if humi is not None and temp is not None :
        print("Temperature: {0:.01f}*C   Humidity: {0:0.1f}%".format(temp,humi))
else :
        print("Gagal Membaca")
    time.sleep(2)

