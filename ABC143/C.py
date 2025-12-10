import itertools
N=int(input())
S=input()
groups=[]

for key,group in itertools.groupby(S):
    grouplist=list(group)
    length=len(grouplist)
    groups.append((key,length))
print(len(groups))
