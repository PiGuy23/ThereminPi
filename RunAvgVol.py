import alsaaudio
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mixer('PCM')


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
    
    vol = round(((avg) * 100) + 30)
    if (vol > 100) :
        vol = 100
    print(vol)
    m.setvolume(vol)
        
    sleep(0.08)


