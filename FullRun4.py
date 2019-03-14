#usr/bin/python3
#Contains RunAvg Volume
#Contains RunAvg Notes
#Contains Synth Switch
#Contains Stop Switch
from setup2 import *

#Time Access
time_interval = .1

#Access array length
vol_arr_length = 5
notes_arr_length = 8

if GPIO.input(20) == GPIO.HIGH:
    runner = prophet_code
    print("Prophet")
elif(GPIO.input(16) == GPIO.HIGH) :
    runner = square_code
    print("Square")
elif(GPIO.input(12) == GPIO.HIGH) :
    runner = chip_lead_code
    print("Chip Lead")
elif (GPIO.input(20) == GPIO.LOW) and (GPIO.input(16) == GPIO.LOW) and (GPIO.input(12) == GPIO.LOW):
    runner = saw_code
    print("Saw")

run(runner)

vals = [0.5] * notes_arr_length
vals2 = [0.5] * vol_arr_length

d = [0.5]
d2 = [0.5]

def average(arr, next, hol):
    k = len(arr) -1
    i = 0
    while i < k:
        arr[i] = arr[i+1]
        i = i+1

    if next == 1.0:
        arr[k] = hol[0]
    else:
        arr[k] = next
        hol[0] = next
    
    j = 0
    for y in arr:
        j = j + y
        
    avg = j/(k+1)
    return avg
    
    
sender.send_message('/play_this', 60)
while True:
    x = (sensor.distance)
    x2 = (sensor2.distance)
    
    #Stop switch
    if GPIO.input(21) == GPIO.HIGH :
        stop()
    #Synth switch
    if (GPIO.input(20) == GPIO.LOW) and (GPIO.input(16) == GPIO.LOW) and (GPIO.input(12) == GPIO.LOW) and (runner != saw_code) :
        runner = saw_code
        stop()
        run(runner)
    elif (GPIO.input(20) == GPIO.HIGH) and (runner != prophet_code):
        runner = prophet_code
        stop()
        run(runner)
    elif (GPIO.input(16) == GPIO.HIGH) and (runner != square_code):
        runner = square_code
        stop()
        run(runner)
    elif (GPIO.input(12) == GPIO.HIGH) and (runner != chip_lead_code):
        runner = chip_lead_code
        stop()
        run(runner)
    #Notes
    p_avg = average(vals, x, d)
    
    pitch = round(p_avg * 100 + 30)
    if (pitch <= 100) :
            sender.send_message('/play_this', pitch)
    
    #Volume
    v_avg = average(vals2, x2, d2)
    
    vol = round(((v_avg) * 100) + 60)
    if (vol > 100) :
        vol = 100
    vol_access.setvolume(vol)
    
    
    
    sleep(time_interval)

