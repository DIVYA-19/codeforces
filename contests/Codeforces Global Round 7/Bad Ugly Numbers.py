t = int(input())
 
for _ in range(t):
    n = int(input())
 
    res = ''
 
    if n == 1:
        print(-1)
    else:
        print('2'+(n-1)*'3')
