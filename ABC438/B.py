N,M=map(int,input().split())
S=input()
T=input()

Slen=len(S)
Tlen=len(T)
ans=1000
for i in range(0,Slen-Tlen+1):
    count=0
    for j in range(0,Tlen):
        count+=(int(S[i+j])-int(T[j]))%10
    ans=min(ans,count)

print(ans)
