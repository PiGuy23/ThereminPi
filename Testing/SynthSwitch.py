#WorksPrettyWell
from gpiozero import DistanceSensor
from time import sleep
from psonic import *

from pythonosc import osc_message_builder
from pythonosc import udp_client



 # Import Raspberry Pi GPIO library

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

code1 = """
use_synth :saw
s = play 60, release: 120, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
"""
code2 = """
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
    runner = code1
    print("Saw")
else :
    runner = code2
    print("Prophet")
run(runner)


sensor = DistanceSensor(echo=24, trigger=25)


vals = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

d = 0.5
sender.send_message('/play_this', 60)
while True:
    if GPIO.input(20) == GPIO.HIGH :
        stop()
    if (GPIO.input(21) == GPIO.HIGH) and (runner == code2) :
        runner = code1
        stop()
        run(runner)
    elif (GPIO.input(21) == GPIO.LOW) and (runner == code1):
        runner = code2
        stop()
        run(runner)
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
    
    pitch = round(avg * 100 + 30)
    if (pitch <= 100) :
            sender.send_message('/play_this', pitch)
        
    sleep(0.08)
