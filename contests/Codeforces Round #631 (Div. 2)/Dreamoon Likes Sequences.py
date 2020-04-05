t = int(input())
 
for _ in range(t):
    d,m = map(int, input().split())
 
    ans = 1
 
    i = 0
    r  = min(2**(i+1) - 1, d) - 2**i + 2
    while(r>0):
        ans *= r
        i += 1
        r  = min(2**(i+1) - 1, d) - 2**i + 2
 
    print((ans-1)%m)
