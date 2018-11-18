#An example of a running avg done with a function

from time import sleep


vals = [1] * 13

d = 1

def f_avg (arr):
    k = len(arr) -1
    i = 0
    while i < k:
        vals[i] = vals[i+1]
        i = i+1
    
    
    x = int(input())
    if x == 1.0:
        vals[k] = d
    else:
        vals[k] = x
        d = x
    
    j = 0
    for y in arr:
        j = j + y
        
    avg = j/(k+1)
    return avg

while True:
    print(f_avg(vals))