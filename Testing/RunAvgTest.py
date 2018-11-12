#Works really well. Thi bigger the better
from time import sleep
vals = [0] * 4
b = 0
while True:
    
    i = 0
    while i < 3:
        vals[i] = vals[i+1]
        i = i+1
    
    x = int(input())
    vals[3] = x
    
    j = 0
    for y in vals:
        j = j + y
        
    avg = j/4
    print(avg)
    
    
    
    
    
    