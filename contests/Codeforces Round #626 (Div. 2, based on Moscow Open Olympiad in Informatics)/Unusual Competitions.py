'''
explanation

we have to find minimum number of nanoseconds(ns) required to make the sequence correct
ex - ))((())(
-- we first reorder the segment from 1st to 4th -> (())())( -> 4 ns
-- then reorder the 7th to 8th -> (())()() -> 2ns
-- ans is 6

I use two stacks here - one for close bracket -> ')' one for open bracket -> '('
1. when we find '(' we store that in stack_open
2. when we find ')' we check stack_open if we have opening brackets before
   - if yes, we del the top from stack_open (as they are a pair '()')
   - if no, we have an balanced close bracket, so we store that in stack_close
3. when we find '(' and stack_close have items in it
   - we perform reorder operation there and both stack tops
   - and increment operations by 2

'''
n = int(input())
 
s = input()
stack_close = []
stack_open = []
pair = 0
 
if s.count(')') != s.count('('):
    print(-1)
else:
    for i in s:
        if i == '(':
            stack_open.append(i)
        if i == ')':
            if stack_open:
                del stack_open[-1]
            else:
                stack_close.append(i)
        elif stack_close and i == '(':
            del stack_close[-1]
            del stack_open[-1]
            pair += 2
    print(pair)
    
