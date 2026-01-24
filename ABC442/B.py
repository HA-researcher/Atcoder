Q=int(input())

volume=0
resume=0
for _ in range(Q):
    A=input()
    if A=="1":
        volume+=1
    elif A=="2":
        if volume!=0:
            volume-=1
    else:
        if resume==1:
            resume=0
        else:
            resume=1
    if (volume>=3) and (resume):
        print("Yes")
    else:
        print("No")
