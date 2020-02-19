import math
n = int(input())

facs = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        facs.append(n//i)
        facs.append(i)
facs = sorted(facs)
for j in range(len(facs)-1, -1, -1):
    flag = 0
    i = 2
    while i*i<= facs[j]:
        #print(i)
        if facs[j]%(i*i) == 0:
            flag = 1
            break
        i+=1
    if flag == 0:
        break
print(facs[j])
        
