##単純な累積和ではTLEする。

N=int(input())
S=input()

AminusB=[0]
for i in range(N):
    if S[i]=="A":
        AminusB.append(AminusB[i]+1)
    elif S[i]=="B":
        AminusB.append(AminusB[i]-1)
    else:
        AminusB.append(AminusB[i])
Count=0
for i in range(N):
    for j in range(i,N):
        if AminusB[j+1]-AminusB[i]>0:
            Count+=1
print(Count)
