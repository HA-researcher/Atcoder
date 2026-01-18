P,Q=map(int,input().split())
S,T,Q=list(input()),list(input()),int(input())
lenS,lenT=len(S),len(T)

for i in range(Q):
    FlagS,FlagT=True,True
    w=input()
    lenw=len(w)
    for j in range(lenw):
        if w[j] not in S:
            FlagS=0
        if w[j] not in T:
            FlagT=0
    if FlagS and FlagT:
        print("Unknown")
    elif FlagS:
        print("Takahashi")
    else:
        print("Aoki")

            
