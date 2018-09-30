import alsaaudio
from gpiozero import DistanceSensor
from time import sleep

sensor3 = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mixer('PCM')

val= .5
nval = .5

while True:
    if(sensor3.distance < 1) :
        nval = (sensor3.distance)
        
        while (((nval - val) > 0.1) or ((val - nval) > 0.1)):
            if ((nval - val) > 0.1) :
                nval = nval - 0.1
                
            if ((val - nval) > .1) :
                nval = nval + 0.1
                
        
        vol = round(((val) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        print(vol)
            
        val = nval
        sleep(.01)
        
        
    else :
        
        vol = round(((val) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        print(vol)
        sleep(.01)


