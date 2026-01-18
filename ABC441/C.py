import sys
input=sys.stdin.readline
N,K,X=map(int,input().split())
A=list(map(int,input().split()))

MinA=0
counter=0
A.sort()
#for i in range(N-K):
#    counter+=1
counter=N-K
for i in range(K-1,-1,-1):
    MinA+=A[i]
    counter+=1
    if MinA>=X:
        print(counter)
        break
if MinA<X:
    print(-1)
    
    
