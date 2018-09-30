from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor = DistanceSensor(echo=17, trigger=4)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

val = .1
nval = .1
while True:
    if(sensor.distance != 1.0) :
        nval = (sensor.distance)
        
        #pitch = round(sensor.distance * 100 + 30)
        #if (pitch <= 80) :
            #sender.send_message('/play_this', pitch)
        while (((nval - val) > 0.1) or ((val - nval) > 0.1)):
            if ((nval - val) > 0.1) :
                nval = nval - 0.1
                
            if ((val - nval) > .1) :
                nval = nval + 0.1
                
        
        pitch = round(val * 100 + 30)
        if (pitch <= 80) :
            sender.send_message('/play_this', pitch)
            
            val = nval
        sleep(.01)
        
        
    else :
        
        pitch = round(val * 100 + 30)
        sender.send_message('/play_this', pitch)
        
        sleep(.01)
        
        
    
        
    
