import math
n,m = map(int, input().split())

a = list(map(int, input().split()))
s = sorted(a)

for i in range(1,n):
    s[i] += s[i-1]

res = [s[0]]

for i in range(1,n):
    f = s[i]
    if i-m>=0:
        t = res[i-m]
    else:
        t = 0
    res.append(f+t)
print(*res, sep=' ')
