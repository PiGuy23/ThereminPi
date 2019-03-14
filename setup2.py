
from gpiozero import DistanceSensor
from time import sleep
from psonic import *
import alsaaudio
from pythonosc import osc_message_builder
from pythonosc import udp_client
 # Import Raspberry Pi GPIO library

import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

sensor = DistanceSensor(echo=24, trigger=25)
sensor2 = DistanceSensor(echo=22, trigger=11)
vol_access = alsaaudio.Mixer('PCM')

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
square_code = """
use_synth :square
s = play 60, release: 1200, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
"""
chip_lead_code = """
use_synth :square
s = play 60, release: 1200, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
"""
runner = ""