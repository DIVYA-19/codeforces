'''

P1 + P2 = a
P1 and P2 are permutations with L1 and L2 as lengths

a will be given, we have to print possible lengths of L1 and L2
First we have to observe that we cannot answer more than 2

we have to know to know how many a number appeared in a
if count(i) > 2, then not possible
Otherwise,
find n such that count(1) = count(2) = ... = count(n) = 2
these numbers will be in both permutations
two ways possible:
L1 = n , L2 = len(a) - n
check if both parts have all numbers in range

L1 = len(a) - n, L2 = n
we have to careful when n is len(a)/2 or n i 0

'''

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
