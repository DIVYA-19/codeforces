t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    
    alpha = [0] * 26
    s= input()
    p = list(map(int, input().split()))

    freq = [0] *n
    for i in range(m):
        freq[p[i]-1] += 1
    freq[n-1] = 1

    for i in range(n-1,0,-1):
        freq[i-1] += freq[i]

    for i in range(n):
        alpha[ord(s[i])-97] += freq[i]
    print(*alpha,sep=' ')
            
