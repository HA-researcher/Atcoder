'''#非常にシンプルな解法（TLE)

NA=list(map(int,input().split(" ")))
N=NA.pop(0)
sum=0
for i in range(N):
	for j in range(N):
#for j in len(NA)がだめな理由が分からない。
		if i!=j:
			sum+=NA[i]*NA[j]
			sum%=(10**9+7)
print(sum)
'''


#アルゴリズム変更

NA=list(map(int,input().split(" ")))
N=NA.pop(0)
total_NA=0
sum=0

for i in range(N):
	total_NA+=NA[i]

for i in range(N):
	sum+=(total_NA-NA[i])*NA[i]
	sum%=(10**9+7)

print(sum)

#過去に、DP（動的計画法）で解くのを見た気がする？DPわからないです。
