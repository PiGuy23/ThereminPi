#Dosent Work

from gpiozero import DistanceSensor
from time import sleep
from psonic import *


sensor = DistanceSensor(echo=17, trigger=4)


val = .1
nval = .1
while True:
    if(sensor.distance != 1.0) :
        nval = (sensor.distance)
        
        
        while (((nval - val) > 0.1) or ((val - nval) > 0.1)):
            if ((nval - val) > 0.1) :
                nval = nval - 0.1
                
            if ((val - nval) > .1) :
                nval = nval + 0.1
                
        
        pitch = round(val * 100 + 30)
        if (pitch <= 80) :
            play(pitch)
            print(pitch)
            val = nval
        sleep(1)
        
        
    else :
        
        pitch = round(val * 100 + 30)
        play(pitch)
        print(pitch)
        sleep(1)
        
        
    
        
    
