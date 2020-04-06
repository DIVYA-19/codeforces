
'''
directions are jumbled in the problem 
a - u-1 v - left -> up - d
b - u+1 v - right -> down - c
c - u, v-1 - down -> left - a
d - u,v+1 - up -> right - b

we can just keep walking b/w two cells (up/dowm and right/left) 
and the remaining walks (up/down/right/left), we need too check if we have that many cells

and basically we need atleast 1 cell other than the present position, if a/b/c/d > 0, to it's corresponding directions 

present - x,y
start   - x1,y1
end     - x2,y2

for up,
no.of cells possible to move -> x - x1

'''
t = int(input())

for _ in range(t):
    d,c,a,b = map(int, input().split())
 
    x,y,x1,y1,x2,y2 = map(int, input().split())
 
    left = y - y1 
    right = y2 - y 
    up = x - x1
    down = x2  - x 
    check = 1
 
#a - 2 b - 2 c - 2 d - 0
    if a > b:
        rem = a - b
        if left < rem:
            check = 0
    elif b > a:
        rem = b - a
        if right < rem:
            check = 0
    else:
        if a and b and y2 - y1 + 1 < 2:
            check = 0
    if c > d:
        rem = c - d
        if down < rem:
            check = 0
    elif d > c:
        rem = d - c
        if up < rem:
            check = 0
    else:
        if c and d and x2 - x1 + 1 < 2:
            check = 0
        
        
 
    if check:
        print("Yes")
    else:
        print("No")
