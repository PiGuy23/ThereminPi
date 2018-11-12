#WorksPrettyWell
import alsaaudio
from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=22, trigger=11)
m = alsaaudio.Mix2er('PCM')


vals2 = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

d2 = 0.5

while True:
    i2 = 0
    while i2 < 8:
        vals2[i2] = vals2[i2+1]
        i2 = i2+1
    
    
    x2 = (sensor.distance)
    if x2 == 1.0:
        vals2[8] = d2
    else:
        vals2[8] = x2
        d2 = x2
    
    j2 = 0
    for y2 in vals2:
        j2 = j2 + y2
        
    avg2 = j/4
    
    vol = round(((avg2) * 100) + 30)
    if (vol > 100) :
        vol = 100
    print(vol)
    m.setvolume(vol)
        
    sleep(0.08)


