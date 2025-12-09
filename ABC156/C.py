N = int(input())
X = list(map(int, input().split()))

#数学的な解法。下に凸なので微分して=0の地点を探すと、sum(X)/Nとわかる。それを最近整数にする。
avg = sum(X) / N
P = round(avg)

ans = sum((x - P)**2 for x in X)

print(ans)
"""
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
"""

