q = int(input())
 
for i in range(q):
    n = int(input())
 
    a = 0
    i = 0
    while(a<n):
        a += (3**i)
        i+=1
    while(i>=0):
        if a - 3**i >=n:
            a -= 3**i
        i-=1
    print(a)
