import itertools

S = input()
ans = []

for key, group in itertools.groupby(S):
    # 文字列を作ってリストに追加
    ans.append(f"{key}{len(list(group))}")
print("".join(ans))
"""
import itertools

S=input()
KeyList=[]

for key,group in itertools.groupby(S):
    print(key,end="")
    print(len(list(group)),end="")
print("\n",end="")
"""
