t = int(input())
for i in range(t):
    s = input()
    start = -1
    end = -1
    count = 0

    for i in range(len(s)):
        if s[i] == '0' and start == -1 and i-1>=0 and s[i-1] == '1':
            start = i
            end = -1
        if s[i] == '1' and end == -1 and start != -1:
            end = i-1
            count += (end-start)+1
            start = -1
        #print(start,end,count)
    
    print(count)
