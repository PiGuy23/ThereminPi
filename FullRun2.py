#usr/bin/python3
#Contains RunAvg Volume
#Contains RunAvg Notes
#Contains Synth Switch
#Contains Stop Switch
from gpiozero import DistanceSensor
from time import sleep
from psonic import *
import alsaaudio
from pythonosc import osc_message_builder
from pythonosc import udp_client

#Time Access
time_interval = .1

#Access array length
vol_arr_length = 10
notes_arr_length = 5

 # Import Raspberry Pi GPIO library

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

saw_code = """
use_synth :saw
s = play 60, release: 120, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
"""
prophet_code = """
use_synth :prophet
s = play 60, release: 1200, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
"""
runner = ""
if GPIO.input(21) == GPIO.HIGH:
    runner = saw_code
    print("Saw")
else :
    runner = prophet_code
    print("Prophet")
run(runner)


sensor = DistanceSensor(echo=24, trigger=25)
sensor2 = DistanceSensor(echo=22, trigger=11)
vol_access = alsaaudio.Mixer('PCM')


vals = [0.5] * notes_arr_length
vals2 = [0.5] * vol_arr_length

d = 0.5
d2 = 0.5
sender.send_message('/play_this', 60)
while True:
    x = (sensor.distance)
    x2 = (sensor2.distance)
    
    #Stop switch
    if GPIO.input(20) == GPIO.HIGH :
        stop()
    #Synth switch
    if (GPIO.input(21) == GPIO.HIGH) and (runner == prophet_code) :
        runner = saw_code
        stop()
        run(runner)
    elif (GPIO.input(21) == GPIO.LOW) and (runner == saw_code):
        runner = prophet_code
        stop()
        run(runner)
    #Notes
    k = len(vals) -1
    i = 0
    while i < k:
        vals[i] = vals[i+1]
        i = i+1
    
    
    
    if x == 1.0:
        vals[k] = d
    else:
        vals[k] = x
        d = x
    
    j = 0
    for y in vals:
        j = j + y
        
    avg = j/(k+1)
    
    pitch = round(avg * 100 + 30)
    if (pitch <= 100) :
            sender.send_message('/play_this', pitch)
    
    #Volume
    k2 = len(vals2) -1
    i2 = 0
    while i2 < k2:
        vals2[i2] = vals2[i2+1]
        i2 = i2+1
    
    
    
    if x2 == 1.0:
        vals2[k2] = d2
    else:
        vals2[k2] = x2
        d2 = x2
    
    j2 = 0
    for y2 in vals2:
        j2 = j2 + y2
        
    avg2 = j2/(k2+1)
    
    vol = round(((avg2) * 100) + 50)
    if (vol > 100) :
        vol = 100
    vol_access.setvolume(vol)
    
    
    
    sleep(time_interval)

