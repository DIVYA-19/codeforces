t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    temps = []

    for _ in range(n):
        temps.append(list(map(int, input().split())))


    lf = m
    ri = m
    t=0
    for i in range(n):
        ti = temps[i][0]
        l = temps[i][1]
        r = temps[i][2]

        dif = ti - t
        lf = max(lf - dif,l)
        ri = min(ri + dif,r)

        if lf>ri:
            print("NO")
            break

        t = ti
    else:
        print("YES")
