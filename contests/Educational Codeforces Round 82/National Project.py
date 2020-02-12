import math
t = int(input())

for i in range(t):
    n,g,b = map(int,input().split())

    h = math.ceil(n/2)
    g_needed = h//g
    remain = h%g
    flag = 0
    if remain:
        flag = 1
    if h<g:
        print(n)
    else:
        #print(g_needed, (b*(g_needed-1+flag)) , remain)
        total = (g * (g_needed)) + (b*(g_needed-1+flag)) + remain + max(0, n-h-(b*(g_needed-1+flag)))
        print(total)
