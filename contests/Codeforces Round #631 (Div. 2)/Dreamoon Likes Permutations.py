t = int(input())
 
for _ in range(t):
    n = int(input())
 
    a = list(map(int, input().split()))
 
    
    flag = 1
    first = 0
    out = 0
    mem = [0] * n
    for i in a:
        mem[i-1] += 1
        if mem[i-1] > 2:
            flag = 0
            break
    for i in mem:
        if i == 2:
            first += 1
        else:
            break
 
    if flag and first and first <= n:
        sec = n - first
        f = a[:first]
        s = a[first:]
        #print(first,sec)
        #print(f,s)
        res = []
        check1 = list(range(1,first+1))
        check2 = list(range(1,sec+1))
 
        if check1 == list(set(f)) and check2 == list(set(s)):
            out = 1
            res.append([first,sec])
        f = a[:sec]
        s = a[sec:]
        #print(f,s)
        if check2 == list(set(f)) and check1 == list(set(s)) and first!=sec:
            out += 1
            res.append([sec,first])
        print(out)
        for i in res:
            print(*i)
    else:
        print(out)
