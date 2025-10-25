import sys
from collections import Counter

N=int(input())
A=input().split(" ")

freq=Counter(A)
count=0

for v_count in freq.values():
	if v_count<2:
		continue
	pair=(v_count)*(v_count-1)/2
	other=N-v_count
	count+=pair*other

print(int(count))
