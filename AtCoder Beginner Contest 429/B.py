NM=input().split(" ")
N=int(NM[0])
M=int(NM[1])
A=input().split(" ")

sum_before=0
sum=0

for i in range(N):
	sum_before+=int(A[i])

for i in range(N):
	sum=sum_before-int(A[i])
	if sum==M:
		print("Yes")
		exit()
print("No")


