#+(A-1)*N

A,B=map(int,input().split())

N=0
while B>1+(A-1)*N:
    N+=1
print(N)
