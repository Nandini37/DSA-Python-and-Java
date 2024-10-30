t = int(input())

while t>0:
    
    N = int(input())
    
    if (N>= 1) :
        if (N % 2 == 1):
            A = (N + 1) // 2
    
        else:
            A = N
            
    t =t-1
    print(A)
