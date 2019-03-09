#Works really well. Thi bigger the better
from time import sleep
vals = [0] * 4
b = 0

def average(arr, next, hol):
    k = len(arr) -1
    i = 0
    while i < k:
        arr[i] = arr[i+1]
        i = i+1
    
    
    
    if next == 1.0:
        arr[k] = hol[0]
    else:
        arr[k] = next
        hol[0] = next
    
    j = 0
    for y in arr:
        j = j + y
        
    avg = j/(k+1)
    return avg
d = [0]
while True:
    
    x = int(input())
    print("Average: ")
    print(average(vals, x, d))
    
    print("\n")
    print("D: ")
    print(d[0])
    print("\n")
    for n in vals:
        print(n)
    print("\n")
    
    
    
    
    