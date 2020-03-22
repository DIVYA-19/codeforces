n = int(input())
 
a = list(map(int, input().split()))
track = 0
res = [0] * n
for i in range(0,n):
    res[i] = a[i] + track
    track = max(res[i], track)
    
print(*res, sep=' ')
