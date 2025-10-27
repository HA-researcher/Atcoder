
"""NM=input().split(" ")
N=int(NM[0])
M=int(NM[1])
mapで1行で受け取れる
"""
N,M=map(int,input().split())


for i in range(N+1):
	for j in range(N-i+1):
		if i*10000+j*5000+(N-i-j)*1000==M:
			print(i j N-i-j)
			exit()
print("-1 -1 -1")


