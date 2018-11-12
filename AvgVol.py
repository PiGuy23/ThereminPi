import alsaaudio
from gpiozero import DistanceSensor
from time import sleep

sensor1 = DistanceSensor(echo=24, trigger=25)
sensor2 = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mixer('PCM')


val= .5
nval = .5

while True:
    if((sensor1.distance < 1)&(sensor2.distance < 1)) :
        nval = (((sensor1.distance)+(sensor2.distance))/2)
        
        while (((nval - val) > 0.1) or ((val - nval) > 0.1)):
            if ((nval - val) > 0.1) :
                nval = nval - 0.1
                
            if ((val - nval) > .1) :
                nval = nval + 0.1
                
        
        vol = round(((val) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        
            
        val = nval
        sleep(.01)
        
        
    else :
        
        vol = round(((val) * 100) + 30)
        if (vol > 100) :
            vol = 100
        m.setvolume(vol)
        
        sleep(.01)


