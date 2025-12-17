"""
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
"""

#よりよいコード
def solve():
    N = int(input())
    S = input().strip()

    # 最初の状態：リーダーは一番左(index 0)
    # コスト = (左側のW=0) + (右側のEの数)
    # 右側(index 1以降)のEの数を数える
    current_cost = S[1:].count('E')
    min_cost = current_cost
    # リーダーを i (0) から i+1 (1) へ動かしていく
    for i in range(N - 1):
        # 1. 旧リーダー (S[i]) が「左側」の集団に入る
        if S[i] == 'W':
            current_cost += 1
        # 2. 新リーダー (S[i+1]) が「右側」の集団から抜けてリーダーになる
        if S[i+1] == 'E':
            current_cost -= 1
        if current_cost < min_cost:
            min_cost = current_cost
    print(min_cost)

solve()
