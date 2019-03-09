#WorksAgain
import alsaaudio
from gpiozero import DistanceSensor
from time import sleep
 
sensor = DistanceSensor(echo=24, trigger=25)
m = alsaaudio.Mixer('PCM')
 
 
vals2 = [0.5] * 15

d2 = 0.5

while True:
    k2 = len(vals2) -1
    i2 = 0
    while i2 < k2:
        vals[i2] = vals[i2+1]
        i2 = i2+1
    
    
    x2 = (sensor2.distance)
    if x2 == 1.0:
        vals[k2] = d2
    else:
        vals[k2] = x2
        d2 = x2
    
    j2 = 0
    for y2 in vals2:
        j2 = j2 + y2
        
    avg2 = j2/(k2+1)
    
    vol = round(((avg2) * 100) + 30)
    if (vol > 100) :
        vol = 100
    m.setvolume(vol)
    
    sleep(0.005)
