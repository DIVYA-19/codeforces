t = int(input())
 
primes = list(range(2,1003))
 
for i in range(2,int(1002**0.5)+1):
    if i in primes:
        j = i*i
        while(j<=1002):
            try:
                primes.remove(j)
            except:
                pass
            j+=i
for _ in range(t):
    n = int(input())
 
    a = list(map(int, input().split()))
    b= [0] * n
    track = 1
 
    for i in primes:
        flag = 0
        for j in range(n):
            if a[j]%i == 0:
                if b[j] == 0:
                    b[j] = track
                    flag = 1
        if flag:
            track += 1
        if b.count(0) == 0:
            break
    print(len(list(set(b))))
    print(*b)
