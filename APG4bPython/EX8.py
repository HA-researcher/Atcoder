N=int(input())
A=[]
for i in range(N):
  A.append(list(map(int,input().split())))
  print(A[i][0]+A[i][1])
