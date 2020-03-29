n = int(input())

b = list(map(int, input().split()))

mem = {}

for i in range(n):
    if i-b[i] not in mem:
        mem[i-b[i]] = 0
    mem[i - b[i]] += b[i]

ans = 0
for i in mem:
    ans = max(ans, mem[i])
print(ans)
