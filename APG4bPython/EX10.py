N = int(input())
# ここにプログラムを追記

A=list(map(int,input().split()))

average=int(sum(A)/N)

for i in range(N):
	if A[i]>=average:
		print(A[i]-average)
	else:
		print(average-A[i])
