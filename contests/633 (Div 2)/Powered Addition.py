'''
we keep track of prefix max
for every i, we will check if a[i] < prefix sum 
if yes, we need to increment a[i]
-- to the value 2**x
-- minimum value of x where 2**x >= prefix sum - a[i]
-- -- x value is msb of (prefix sum - a[i])

'''

import math
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = 0
    max_so_far = a[0]

    for i in range(1,n):
        if a[i]<max_so_far:

            max_so_far = max(max_so_far,a[i-1])
            m = max(m,int(math.log2(max_so_far-a[i])) + 1)
    
    print(m)
