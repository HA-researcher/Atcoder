N=int(input())
A=list(map(int,input().split()))

Zahyou=dict()
Zahyou[1]=A[0]+1
for i in range(1,N):
    Zahyou[i+1]=max(A[i]+i+1,Zahyou[i])
Count=1
for i in range(2,N+1):
    if Zahyou[i-1]>i:
        Count+=1
    else:
        break
print(Count)
