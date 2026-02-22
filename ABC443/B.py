N,K=map(int,input().split())

count=1
newN=N
while newN<K:
    newN+=N+count
    count+=1

print(count-1)

