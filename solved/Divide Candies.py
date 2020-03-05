n,m = map(int, input().split())
out = 0
for i in range(1,min(m,n)+1):
    for j in range(1,min(m,n)+1):
        if (i*i + j*j) % m==0:
            out += ((n-i)//m +1) * ((n-j)//m +1)

print(out)
