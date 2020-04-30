'''
a -> saorted values
greatest difference elements will be at the end, a[0],a[n]
third element from the last will be a[n-1]
so that |a[n-1]-a[0]| <= |a[0]-a[n-1]|
4th will be a[1], a[1] is bigger than a[0]  -> |a[1]-a[n-1]| <= |a[n-1]-a[0]|
'''

t = int(input())
 
for _ in range(t):
    n = int(input())
 
    a = list(map(int, input().split()))
 
    sortedA = sorted(a)
 
    ans = [0] * n
 
    i = 0
    j = n-1
    idx = n-1
    while i<=j:
        ans[idx] = sortedA[j]
        idx -= 1
        if(i!=j):
            ans[idx] = sortedA[i]
            idx -= 1
        i += 1
        j -= 1
    print(*ans)
