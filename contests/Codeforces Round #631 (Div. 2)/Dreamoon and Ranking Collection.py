'''
we can add x more elements to the list a 
and find the greatest n, such that a should contain 1 to n elements

loop from 1 to len(a) + x 
we can't have n > len(a) +x
'''
t = int(input())
 
for _ in range(t):
    n,x = map(int, input().split())
 
    a = list(map(int, input().split()))
    a_s = set(a)
    i = 1
    s = 0
    dup_x = x
 
    while(i<=n+dup_x):
 
        if i in a_s:
            s += 1
        else:
            if x <=0:
                break
            x -= 1
            s += 1
        i+=1
    print(s)
