'''
s is k-complete word
- s is a palindrome
- s has a period of k, i.e. si=sk+i for all 1≤i≤n−k

if s is k-complete
then it will have k length palindromes sequently
Ex:  k = 3, abaaba , (1,3) -> palindrome (4,6) -> palindrome

 
si = s(k+i) = s(k-i-1+k) = s(k-i-1) for all i = 0,..,k//2
if k is even we are good, if k is odd we have to check min replaces separately
we have to min possible replaces for every i and add them to get ans
'''
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
