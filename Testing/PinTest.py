from gpiozero import DistanceSensor
from time import sleep


sensor1 = DistanceSensor(echo=22, trigger=11)
sensor = DistanceSensor(echo=24, trigger=25)
#18 and 23
#17and 4
#22 and 11
#24 and 25
while True:
    x = sensor.distance
    y = sensor1.distance
    
    print("Right")
    print (x)
    print("lLeft")
    print (y)
    print("\n")
    
    sleep(1)
