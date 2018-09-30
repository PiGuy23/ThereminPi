from gpiozero import DistanceSensor
from time import sleep

from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor2 = DistanceSensor(echo=22, trigger=11)
sender2 = udp_client.SimpleUDPClient('127.0.0.1', 4559)

val2 = .05
nval2 = .05

while True:
    if(sensor2.distance != 1.0) :
        nval = (sensor2.distance)
        
        #pitch = round(sensor.distance * 100 + 30)
        #if (pitch <= 80) :
            #sender.send_message('/play_this', pitch)
        while (((nval2 - val2) > 0.1) or ((val2 - nval2) > 0.1)):
            if ((nval2 - val2) > 0.1) :
                nval2 = nval2 - 0.1
                
            if ((val2 - nval2) > .1) :
                nval2 = nval2 + 0.1
                
        
        
        sender2.send_message('/vol', val2)
        
        val2 = nval2
        sleep(.01)
        
        
    else :
        
        
        sender2.send_message('/vol', val2)
        
        
        
        sleep(.01)
    
        
    

