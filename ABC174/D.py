N=int(input())
C=input()
#白石を全部右に移動させるか
#白石を全部赤にする
CountW=0
CountR=0

M=0
for i in range(N):
    if C[i]=="R":
        M+=1
for i in range(0,M):
    if C[i]=="W":
        CountW+=1
        
print(CountW)
