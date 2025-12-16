N,M,K=map(int,input().split())
H=list(map(int,input().split()))
B=list(map(int,input().split()))

H.sort(reverse=True)
B.sort(reverse=True)

Check=0
j=0
i=0
while i<M and i+j<N:
    if i+j<N and (H[i+j]<=B[i]):
        Check+=1
        i+=1
    else:
        j+=1
if Check>=K:
    print("Yes")
else:
    print("No")
    
    
