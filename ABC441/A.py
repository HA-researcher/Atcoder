P,Q=map(int,input().split())
X,Y=map(int,input().split())

FlagX,FlagY=False,False
now_count=0
while now_count<100:
    if X==P:
        FlagX=True
    if Y==Q:
        FlagY=True
    P,Q,now_count=P+1,Q+1,now_count+1
    
if FlagX and FlagY:
    print("Yes")
else:
    print("No")
