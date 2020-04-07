'''
we keep track of directions 
- x -> horizontal
  inc for left
  dec for right
- y -> vertical
  inc for up
  dec for down
 
(x,y) will be position we'll be at after i steps
we check if we already been at that position before, that means values between prev(x,y) and present (x,y) are canceled out
we take that length and find which is minimum

'''
t = int(input())

for _ in range(t):
    n = int(input())

    s = input()

    x = 0
    y = 0

    d = {}
    d[(0,0)] = -1
    ans = float('INF')

    for idx,i in enumerate(s):
        if i == 'L':
            x += 1
        elif i == 'R':
            x -= 1

        elif i == 'U':
            y += 1
        elif i == 'D':
            y -= 1

        if (x,y) in d:
            prev = d[(x,y)] + 1
            dt = idx - prev +1;

            if (dt < ans):

                ans = dt
                left = prev +1
                right = idx + 1
        d[(x,y)] = idx
        
    if ans > n:
        print(-1)
    else:
        print(left, right)
