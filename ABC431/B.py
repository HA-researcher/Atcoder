import itertools
X=int(input())
N=int(input())
W=list(map(int,input().split()))
Q=int(input())
P=[]
CheckSet=set()
for _ in range(Q):
    P=int(input())
    if P in CheckSet:
        X-=W[P-1]
        CheckSet.remove(P)
    else:
        X+=W[P-1]
        CheckSet.add(P)
    print(X)
