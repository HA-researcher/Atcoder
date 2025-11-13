N,M=list(map(int,input().split()))
A=[0]*(M+1)
B=[0]*(M+1)
for i in range(M):
  A[i],B[i]=list(map(int,input().split()))

search=set()
search2=set()
for i in range(M):
  if B[i]==N:
    search.add(A[i])
  if A[i]==1:
    search2.add(B[i])

for i in search:
  if i in search2:
    print("POSSIBLE")
    exit()

print("IMPOSSIBLE")




"""
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
"""
