m,n,ta,tb,k = map(int, input().split())
 
a = list(map(int, input().split()))
 
b = list(map(int, input().split()))
 
if m<=k:
    print(-1)
else:
    ans = 0
    count = 0
    bef = 0
    for i in range(m):
        now = a[i]
        #print('count',count)
        for j in range(bef,n):
            if b[j] < a[i] + ta:
                if j==n-1:
                    j+=1
                pass
            else:
                #print('b',a[i]+ta,b[j])
                break
        #print(j, k - count)
        if count>k:
            break
        if j==n:
            ans = 0
            break
        if k - count < n-j:
            #print('k',k-count,n-j)
            ans = max(ans, b[j+k-count]+tb)
        else:
            ans = 0
            break
        bef = j
        count += 1
    if ans == 0:
        print(-1)
    else:
        print(ans)
