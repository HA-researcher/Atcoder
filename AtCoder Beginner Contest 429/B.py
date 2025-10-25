N=int(input())
A=input().split(" ")

count=0

for i in range(N):
	for j in range(N):
		if i==j:
			break
		if A[i]==A[j]:
			for k in range(N):
				if k!=i && k!=j:
					if A[k]!=A[j]:
						count+=1
					

print(count)
