
from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(echo=17, trigger=4)
sensor2 = DistanceSensor(echo=22, trigger=11)



while True:
    x = sensor1.distance
    y = sensor2.distance
    print(x)
    print(y)
    sleep(1)



