N=int(input())
A=list(map(int,input().split()))

A_partsum=[]
Count=0
for l in range(N):
    for r in range(l,N):
        for i in range(l,r+1):
            if sum(A[l:r+1])%A[i]==0:
                break
            elif i==r:
                Count+=1
                
print(Count)
