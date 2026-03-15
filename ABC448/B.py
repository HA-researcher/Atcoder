N,X=map(int,(input().split()))
C=list(map(int,input().split()))

sums=0
for i in range(N):
    A,B=map(int,input().split())
    waste=min(C[A-1],B)
    C[A-1]-=waste
    sums+=waste
print(sums)
