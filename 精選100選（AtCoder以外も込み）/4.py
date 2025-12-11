#https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c

N,M=map(int,input().split())
A=[]

ans=0
for i in range(N):
    total=0
    A.append(list(map(int,input().split())))
    #ここまででA[N-1][M-1]までリスト入ってる
Max=0
for i in range(M):
    for j in range(i,M):
        Total=0
        for k in range(N):
            Total+=max(A[k][i],A[k][j])
        Max=max(Max,Total)
print(Max)

#12分でコーディング。全探索は十分と判断し、精選の１～３は飛ばすことにする。
