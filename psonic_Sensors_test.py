#Kind of Works Now

from gpiozero import DistanceSensor
from time import sleep
from psonic import *


sensor = DistanceSensor(echo=17, trigger=4)


pitch = 60
while True:
    if(sensor.distance != 1.0) :
        val = (sensor.distance)
        
        
                
        
        pitch2 = round(val * 100 + 30)
        while ((pitch - pitch2) > 1) or ((pitch2 - pitch) > 1): 
            if ((pitch - pitch2) > 1):
                pitch2 += 1
            if ((pitch2 - pitch) > 1):
                pitch2 -= 1
        pitch = pitch2
        if (pitch <= 80) :
            play(pitch, release=0.5)
        sleep(0.05)
        
        
    
    
        
        
    
        
    
