from psonic import *
from pythonosc import osc_message_builder
from pythonosc import udp_client
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

run("""
use_synth :saw
s = play 60, release: 20, note_slide: 0.1

live_loop :listen do
use_real_time
  
msg = sync "/osc/play_this"
  
control s, note: msg, amp: 0.5
  
  
  
end
""")

while True:
    
    pitch = int(input())
    print(pitch)
    sender.send_message('/play_this', pitch)
    
    
    
    
