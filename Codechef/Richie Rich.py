t = int(input())

while t > 0:
    s = input("")
    arr = s.split(" ")
    
    A = int(arr[0])
    B = int(arr[1])
    X = int(arr[2])
    
    print(int((B-A)/X))
    
    t = t-1
