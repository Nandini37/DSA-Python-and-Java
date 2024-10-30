### Vaccine Dates

Here is the problem statement:
[Codechef]()

---
#### Python Solution

```
t = int(input())

while t > 0:
    s = input("")
    arr = s.split(" ")
    
    D = int(arr[0])
    L = int(arr[1])
    R = int(arr[2])
    
    if D<L:
        print("Too Early")
    elif D>R:
        print("Too Late")
    else:
        print("Take second dose now")
        
    t = t-1

```
