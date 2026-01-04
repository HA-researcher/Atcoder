import sys
from collections import defaultdict
from bisect import bisect_left

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

pos7=defaultdict(list)
pos5=defaultdict(list)
pos3=defaultdict(list)

for i, x in enumerate(A):
    if x%7==0:
        pos7[x//7].append(i)
    if x%5==0:
        pos5[x//5].append(i)
    if x%3==0:
        pos3[x//3].append(i)
ans=0
for base, j_list in pos5.items():
    list7=pos7[base]
    list3=pos3[base]
    
    if not list7 or not list3:
        continue
    for j in j_list:
        cnt7_left=bisect_left(list7, j)
        cnt3_left=bisect_left(list3, j)
        cnt7_right=len(list7)-cnt7_left
        cnt3_right=len(list3)-cnt3_left
        ans+=cnt7_left*cnt3_left
        ans+=cnt7_right*cnt3_right
print(ans)
