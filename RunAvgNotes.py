#WorksPrettyWell
from gpiozero import DistanceSensor
from time import sleep
from psonic import *

sensor = DistanceSensor(echo=24, trigger=25)


vals = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

d = 0.5

while True:
    i = 0
    while i < 8:
        vals[i] = vals[i+1]
        i = i+1
    
    
    x = (sensor.distance)
    if x == 1.0:
        vals[8] = d
    else:
        vals[8] = x
        d = x
    
    j = 0
    for y in vals:
        j = j + y
        
    avg = j/4
    
    pitch = round(avg * 100 + 30)
    if (pitch <= 80) :
            play(pitch, release=0.5)
        
            
    sleep(0.08)
