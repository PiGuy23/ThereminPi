from gpiozero import DistanceSensor
#18 and 23
#17and 4
#22 and 1
#24 and 25

sensor1 = DistanceSensor(echo=24, trigger=25)

print (sensor1.distance)