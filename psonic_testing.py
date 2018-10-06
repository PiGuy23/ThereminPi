from psonic import *
from time import sleep
use_synth(SAW)
i = 60
while (i < 70):
    
    
    play(i, release=0.1)
    
    
    i += 2
    
    
    sleep(1)
    
    