#WorksPrettyWell
from gpiozero import DistanceSensor
from time import sleep
from psonic import *
from pythonosc import osc_message_builder
from pythonosc import udp_client
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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


vals = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

d = 0.5
sender.send_message('/play_this', 60)
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
    
    pitch = round(avg * 100 + 30)
    if (pitch <= 150) :
            sender.send_message('/play_this', pitch)
        
    if (GPIO.input(21) == GPIO.HIGH):
        code = """
        use_synth :prophet
        s = play 60, release: 20, note_slide: 0.1

        live_loop :listen do
        use_real_time
  
        msg = sync "/osc/play_this"
  
        control s, note: msg, amp: 0.5
  
  
  
        end"""
        print("prophet")
    else:
        code = """
        use_synth :saw
        s = play 60, release: 20, note_slide: 0.1

        live_loop :listen do
        use_real_time
  
        msg = sync "/osc/play_this"
  
        control s, note: msg, amp: 0.5
  
  
  
        end"""
        print("saw")
    sleep(0.08)
