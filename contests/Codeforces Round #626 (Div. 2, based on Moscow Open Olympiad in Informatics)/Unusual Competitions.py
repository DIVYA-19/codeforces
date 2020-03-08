n = int(input())
 
s = input()
stack = []
stack2 = []
pair = 0
 
if s.count(')') != s.count('('):
    print(-1)
else:
    for i in s:
        if i == '(':
            stack2.append(i)
        if i == ')':
            if stack2:
                del stack2[-1]
            else:
                stack.append(i)
        elif stack and i == '(':
            del stack[-1]
            del stack2[-1]
            pair += 2
    print(pair)
    
