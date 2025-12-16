N,M,K=map(int,input().split())
H=list(map(int,input().split()))
B=list(map(int,input().split()))

H.sort(reverse=True)
B.sort(reverse=True)

Check=0

ind_N=0
ind_M=0
while ind_N<N and ind_M<M:
    if H[ind_N]<=B[ind_M]:
        Check+=1
        ind_N+=1
        ind_M+=1
    else:
        ind_N+=1
"""
j=0
i=0
while i<M and i+j<N:
    if i+j<N and (H[i+j]<=B[i]):
        Check+=1
        i+=1
    else:
        j+=1
"""
if Check>=K:
    print("Yes")
else:
    print("No")
    
    
