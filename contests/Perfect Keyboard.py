import math
t = int(input())

class Node():
    def __init__(self,val):
        self.val = val
        self.right = None
        
for i in range(t):
    s = input()
    s = list(s)
    keyboard = ''
    head = Node(s[0])
    added = [s[0]]
    flag = 0
    d = {}

    for i,item in enumerate(s):
        if i==0:
            continue
        temp = head
        node = Node(item)
        prev = None
        
        if i-1>=0 and head.val == s[i-1] and head.right != None and item not in added:
            added.append(item)
            node.right = head
            head = node
        else:
            while(temp!=None):
                if temp.val == s[i-1] and prev != item:
                    if temp.right == None:
                        if item not in added:
                            temp.right = node
                            added.append(item)
                        else:
                            flag = 1
                    else:
                        if temp.right.val == item:
                            pass
                        else:
                            flag = 1
                prev = temp.val
                temp = temp.right
        if flag == 1:
            break
    
    if flag != 1:
        temp = head
        while(temp!=None):
            keyboard += temp.val
            temp = temp.right
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i not in keyboard:
                keyboard += i
        print("YES")
        print(keyboard)
    else:
        print("NO")
        
        
        
        
        
        
        
        
