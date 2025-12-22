H,W,N=map(int,input().split())

A=[]
for i in range(H):
    A.append(set(map(int,input().split())))
B=set()
for i in range(N):
    B.add(int(input()))
ans=0
for i in range(H):
    items=A[i]&B
    ans=max(ans,len(items))
print(ans)
