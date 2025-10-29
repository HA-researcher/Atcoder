"""自力AC
NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]
A=[0]*N
for i in range(N):
	A[i]=list(map(int,input().split()))

A.sort()

number=0
sum=0

while number<M:
	for i in range(N):
		while A[i][1]>0:
			number+=1
			A[i][1]-=1
			sum+=A[i][0]
			if number==M:
			    break
		if number==M:
		    break

print(sum)

よりよいコード
"""

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

A.sort() # O(N log N)

total_cost = 0
drinks_bought = 0 # 現在買った本数 (number)

# 購入ループ O(N)
for i in range(N):
    price = A[i][0]
    stock = A[i][1]
    
    # あと何本必要か
    need_to_buy = M - drinks_bought
    
    # この店で実際に買う本数
    # (在庫すべて か、 必要分だけ の、少ない方)
    buy_amount = min(stock, need_to_buy)
    
    # まとめ買い
    total_cost += price * buy_amount
    drinks_bought += buy_amount
    
    # M本買い終わったら、ループを抜ける
    if drinks_bought == M:
        break

print(total_cost)
