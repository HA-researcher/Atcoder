N,M=map(int,input().split())

#list[i-1]に,iの利害関係者を全部いれる
#list内はsetでいい

conflicts=[set() for _ in range(N)]
for i in range(M):
    A,B=map(int,input().split())
    #print(A,B)
    conflicts[A-1].add(B)
    conflicts[B-1].add(A)
    #print(conflicts)
noconflicts=[0]*N
#print(conflicts)
for i in range(N):
    noconflicts[i]=int((N-len(conflicts[i])-1)*(N-len(conflicts[i])-2)*(N-len(conflicts[i])-3)/6)
print(*noconflicts)
