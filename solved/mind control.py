t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())

    a = list(map(int, input().split()))

    before = m-1
    k = min(k,m)

    temp = [max(a[i],a[n+i-1-before]) for i in range(before+1)]

    if k >= before:
        print(max(temp))
    elif k == 0:
        print(min(temp))
    else:
        temp2 = [min(temp[j:before+1-k+j]) for j in range(k+1)]
        print(max(temp2))
