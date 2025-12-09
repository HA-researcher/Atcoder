S=list(input())
CountB=0
ans=0
for i in range(len(S)):
    if S[i]=="B":
        CountB+=1
    if S[i]=="W":
        ans+=CountB
print(ans)
    
