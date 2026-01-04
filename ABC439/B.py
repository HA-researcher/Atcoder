N=input()
seen=set()
flag=1
newN=0
while flag:
    for i in range(len(N)):
        newN+=int(N[i])**2
    if newN in seen:
        print("No")
        flag=0
    if newN==1:
        print("Yes")
        flag=0
    seen.add(newN)
    N=str(newN)
    newN=0
