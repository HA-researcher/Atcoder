NM=input().split(" ")
N=int(NM[0])
M=int(NM[1])


for i in range(N):
	if i<M:
		print("OK")
	else:
		print("Too Many Requests")
