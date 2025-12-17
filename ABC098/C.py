#ABC098 C - Attention
from collections import Counter
N=int(input())
S=input()
Wcheck=[0]
for i in range(len(S)):
    if S[i]=="W":
        Wcheck.append(Wcheck[i]+1)
    else:
        Wcheck.append(Wcheck[i])
AnsSet=set()

for i in range(1,N+1):
    AnsSet.add((Wcheck[i-1])+(N-i-Wcheck[N]+Wcheck[i]))
print(min(AnsSet))
