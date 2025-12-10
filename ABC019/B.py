import itertools

S=input()
KeyList=[]

for key,group in itertools.groupby(S):
    print(key,end="")
    print(len(list(group)),end="")
print("\n",end="")
