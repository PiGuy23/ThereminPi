#Basic Volume + Notes

import alsaaudio
from gpiozero import DistanceSensor
from time import sleep
from psonic import *


sensor = DistanceSensor(echo=24, trigger=25)
sensor2 = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mixer('PCM')

pitch = 60
val2 = .5
nval2 = .5
while True:
    #Notes

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
        
    
    #Volume
    if(sensor2.distance < 1) :
        nval2 = (sensor2.distance)
        while (((nval2 - val2) > 0.1) or ((val2 - nval2) > 0.1)):
            if ((nval2 - val2) > 0.1) :
                nval2 = nval2 - 0.1 
            if ((val2 - nval2) > .1) :
                nval2 = nval2 + 0.1
        vol = round(((val2) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        val2 = nval2
        
    else :
        vol = round(((val2) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        
    #Universal Sleep
    sleep(.01)
        
    
    