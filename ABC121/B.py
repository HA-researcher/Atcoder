N,M,C=map(int,input().split())
B=list(map(int,input().split()))
A=[]
ans=0
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    total=0
    for j in range(M):
        total+=A[i][j]*B[j]
    if total+C>0:
        ans+=1
print(ans)
