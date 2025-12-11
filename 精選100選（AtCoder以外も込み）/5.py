#https://atcoder.jp/contests/abc095/submissions/71624073
A,B,C,X,Y=map(int,input().split())

#A,BをX,Y枚。2*CでA,Bが1枚ずつ

CountX=0
CountY=0
ans=A*X+B*Y
for i in range(max(X+1,Y+1)):
    money=C*2*i+A*max(X-i,0)+B*max(Y-i,0)
    ans=min(ans,money)
print(ans)
#10分でAC
