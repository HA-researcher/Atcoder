import sys
N=int(input())
#i番目を押すとa[i]番目が光る
a=[]
for j in range(N):
    a.append(int(input()))

current = 1
count = 0

# N回移動してcurrent=２にたどり着かなければループしているので終了してよい
for _ in range(N):
    if current == 2:
        print(count)
        sys.exit()
        
    current = a[current - 1]
    count += 1
    
print(-1)

"""
#a[k]==2かつ、a[j]==k,a[n]==j,....a[1]==l
#もしくはa[1]=l,a[l]=h,a[h]=....a[g]==2
k=1
SetA=set()
Count=0
while Count<N:
    if a[k-1] in SetA:
        print("-1")
        sys.exit()
    SetA.add(a[k-1])
    if a[k-1]==2:
        print(len(SetA))
        sys.exit()
    k=a[k-1]
    Count+=1

"""
