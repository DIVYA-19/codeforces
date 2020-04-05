t = int(input())
 
for _ in range(t):
    n,k = map(int, input().split())
 
    s = input()
    c = 0
 
    for i in range(0,k//2):
        d = {}
        g = 0
        for j in range(i,n,k):
            g+=1
            if s[j] not in d:
                d[s[j]] = 0
            d[s[j]] += 1
        for j in range(k-i-1,n,k):
            g+=1
            if s[j] not in d:
                d[s[j]] = 0
            d[s[j]] += 1
        m = max(d.values())
        #print(m)
        m = g-m
        #print(g,m)
        c+=m
    if k%2 != 0:
        re = k//2
        g = 0
        d = {}
        for i in range(re,n,k):
            g += 1
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
        m = max(d.values())
        m = g-m
        c+=m
    print(c)
