t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    noOfSubs = 1 << n
 
    subs = []
 
    for i in range(0,noOfSubs):
        pos = n-1
        bit = i
        temp = []
        poses = []
        while(bit>0):
            if bit & 1 == 1:
                temp.append(a[pos])
                poses.append(pos+1)
            bit >>= 1
            pos -= 1
        subs.append(temp)
        if temp and sum(temp)%2 == 0:
            print(len(temp))
            print(*sorted(poses), sep=' ')
            break
    else:
        print(-1)
