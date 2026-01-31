'''#非常にシンプルな解法（TLE)

NA=list(map(int,input().split(" ")))
N=NA.pop(0)
sum=0
for i in range(N):
	for j in range(N):
		if i!=j:
			sum+=NA[i]*NA[j]
			sum%=(10**9+7)
print(sum)



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
'''
#上記、都度/2することでfloatになってしまうのでダメ。

MOD = 10**9 + 7
N = int(input())
A = list(map(int, input().split()))

# S = A[0]からA[N-1]までの全ての合計
S = sum(A) % MOD 

ans = 0
for i in range(N):
    # まず、全体の合計Sから自分A[i]を引く
    # これで S は (A[i+1] + ... + A[N-1]) の合計になる
    # (引き算のMODは、マイナスにならないよう +MOD しておくと安全)
    S = (S - A[i] + MOD) % MOD 
    
    # A[i] * (自分より後ろの合計)
    term = (A[i] * S) % MOD
    ans = (ans + term) % MOD

print(ans)
