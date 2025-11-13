#TLEする

N,M=list(map(int,input().split()))
A=[0]*(M+1)
B=[0]*(M+1)
for i in range(M):
  A[i],B[i]=list(map(int,input().split()))

search=0
for i in range(M):
  if B[i]==N:
    search=A[i]
    for j in range(M):
      if A[j]==1 and B[j]==search:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
