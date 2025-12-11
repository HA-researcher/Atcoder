N, M, C=map(int,input().split())
B=list(map(int,input().split()))
ans=0
for _ in range(N):
    A=list(map(int,input().split()))
    score=sum(a*b for a, b in zip(A, B))+C
    if score>0:
        ans+=1
print(ans)

"""
N,M,C=map(int,input().split())
B=list(map(int,input().split()))

ans=0
for i in range(N):
    total=0
    A=list(map(int,input().split()))
    for j in range(M):
        total+=A[j]*B[j]
    if total+C>0:
        ans+=1
print(ans)

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
"""
