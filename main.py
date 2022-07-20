import time
import Adafruit_DHT

sens = Adafruit_DHT.DHT11
gpio = 4

try:
    while True:
        humi, temp = Adafruit_DHT.read(sens, gpio)
        if humi is not None and temp is not None :
            print("Temperature: {0:.01f}*C   Humidity: {0:0.1f}%".format(temp,humi))
        
                # menambah logic untuk print suatu keadaan suhu 
                # jika: suhu kurang dari || lebih dari sekian temperatur
                if temp <= 34 and temp >= 15:
                    print("Suhu aman")
                elif temp >= 34 and temp <= 45:
                    print("Suhu panas")
                elif temp <= 15 and temp >= -15 :
                    print("Suhu dingin")
                else:
                    print("Suhu tidak aman, membahayakan")

            else:
        print("Tidak bisa membaca data dari sensor")
        time.sleep(1)
    
    
# Menghentikan program dengan CTRL + C
    except KeyboardInterrupt:
    print("Sensor dihentikan")