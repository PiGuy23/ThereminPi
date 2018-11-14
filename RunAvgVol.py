#WorksAgain
import alsaaudio
from gpiozero import DistanceSensor
from time import sleep
 
sensor = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mixer('PCM')
 
 
vals = [0.5] * 15

d = 0.5

while True:
    k = len(vals) -1
    i = 0
    while i < k:
        vals[i] = vals[i+1]
        i = i+1
    
    
    x = (sensor.distance)
    if x == 1.0:
        vals[k] = d
    else:
        vals[k] = x
        d = x
    
    j = 0
    for y in vals:
        j = j + y
        
    avg = j/(k+1)
    
    vol = round(((avg) * 100) + 30)
    if (vol > 100) :
        vol = 100
    m.setvolume(vol)
    
    sleep(0.005)
