T=int(input())

for i in range(T):
    CaseN=int(input())
    Case=list(map(int,input().split()))
    NewCase=list(Case)
    Counts=0
    for i in range(CaseN-1):
        if NewCase[i+1]-NewCase[i]>1:
            NewCase[i+1]=NewCase[i]+1
    for i in range(CaseN-1,0,-1):
        if NewCase[i]-NewCase[i-1]<-1:
            NewCase[i-1]=NewCase[i]+1
    
    for i in range(CaseN):
        Counts+=-NewCase[i]+Case[i]


    print(Counts)
    
