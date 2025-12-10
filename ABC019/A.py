lists=list(map(int,input().split()))
lists.sort()
N=len(lists)
print(lists[(N-1)//2])

