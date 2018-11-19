#An example of a running avg done with a function

from time import sleep


vals = [1] * 13
vals2 = [3] * 4

d = 1
d2 = 4

def f_avg (arr):
    k = len(arr) -1
    i = 0
    while i < k:
        arr[i] = arr[i+1]
        i = i+1
    
    global d
    global d2
    x = int(input())
    if (k == 12) :
        if x == 1.0: 
            arr[k] = d
        else:
            arr[k] = x 
            d = x
    else:
        if x == 1.0: 
            arr[k] = d2
        else:
            arr[k] = x 
            d2 = x
    
    j = 0
    for y in arr:
        j = j + y
        
    avg = j/(k+1)
    return avg

while True:
    print(f_avg(vals2))
    