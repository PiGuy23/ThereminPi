#WorksPrettyWell
from gpiozero import DistanceSensor
from time import sleep
from psonic import *
from pythonosc import osc_message_builder
from pythonosc import udp_client




sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

code = """use_synth :saw
s = play 60, release: 20, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end"""
run(code)
sensor = DistanceSensor(echo=24, trigger=25)


vals = [0.5] * 3

d = 0.5
sender.send_message('/play_this', 60)
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
    
    pitch = round(avg * 100 + 30)
    if (pitch <= 150) :
            sender.send_message('/play_this', pitch)
        
    
    sleep(0.08)
