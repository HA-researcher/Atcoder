#ABC122 C - GeT AC
N,Q=map(int,input().split())
S=input()
ATcount=[0]
for i in range(1,len(S)):
    if S[i-1]=="A" and S[i]=="C":
        ATcount.append(ATcount[i-1]+1)
    else:
        ATcount.append(ATcount[i-1])

for _ in range(Q):
    l,r=map(int,input().split())
    l-=1
    r-=1
    if l-1>=0 and (ATcount[l-1]==ATcount[l]):
        print(max(ATcount[r]-ATcount[l],0))
    else:
        print(max(ATcount[r]-ATcount[l],0))



