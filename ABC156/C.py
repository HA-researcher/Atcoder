
N=int(input())
X=list(map(int,input().split()))

MINHP=0
for i in range(N):
    MINHP+=(X[i]-1)**2

MINX=min(X)
MAXX=max(X)
MINP=MAXX
for P in range(MINX,MAXX+1):
    SUM=0
    for i in range(N):
        SUM+=(X[i]-P)**2
    MINHP=min(MINHP,SUM)
    MINP=min(MINP,P)

    
print(MINHP)


