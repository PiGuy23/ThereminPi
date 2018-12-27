#Kind of Works Now

from gpiozero import DistanceSensor
from time import sleep
from psonic import *
from pythonosc import osc_message_builder
from pythonosc import udp_client
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

sensor = DistanceSensor(echo=24, trigger=25)
run("""
use_synth :saw
s = play 60, release: 20, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
""")

pitch = 60
sender.send_message('/play_this', pitch)
while True:
    if(sensor.distance != 1.0) :
        val = (sensor.distance)
        
        
                
        
        pitch2 = round(val * 100 + 30)
        sender.send_message('/play_this', pitch2)
        #while ((pitch - pitch2) > 1) or ((pitch2 - pitch) > 1): 
        #    if ((pitch - pitch2) > 1):
        #        pitch2 += 1
        #    if ((pitch2 - pitch) > 1):
        #        pitch2 -= 1
        #pitch = pitch2
        #if (pitch <= 80) :
        #    sender.send_message('/play_this', pitch)
        sleep(0.1)
        
        
    
    
        
        
    
        
    
