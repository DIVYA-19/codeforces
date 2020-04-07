'''
It's basically same as finding the maximum jars full are possible
so, we have to check first first half from begining(prefix sum) and the second half from the ending(suffix sum)

this should be satisfied
prefix_1 + suffix_1 = prefix_2 + suffix_2 

Let's change the formula as
prefix_1 - prefix_2 = suffix_2 - suffix_1


'''
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    suffix_1 = 0
    suffix_2 = 0
    max_remaning = 0
 
    # s1 + p1 = s2 + p2 -> s1-s2 = p2 - p1
    d = {}
 
    for i in range(2*n-1,n-1,-1):
        #print(i)
        if a[i] == 1:
            suffix_1 += 1
        else:
            suffix_2 += 1
        d[suffix_1 - suffix_2] = i
        if suffix_1 == suffix_2:
            max_remaning = max(max_remaning, 2*n - i)
 
    prefix_1 = 0
    prefix_2 = 0
    #print(d)
 
    
 
    for i in range(n):
        if a[i] == 1:
            prefix_1 += 1
        else:
            prefix_2 += 1
 
        dif = prefix_2 - prefix_1
        #print(dif)
        if (prefix_1 == prefix_2):
            max_remaning = max(max_remaning, i+1)
        if dif in d:
            here = i +1 + (2*n - d[dif])
            max_remaning = max(max_remaning, here)
 
    print(2*n - max_remaning)
