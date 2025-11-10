F,E,D,C,B,A=list(map(int,input().split()))
N=int(input())
Price=[]
Price=list(map(int,input().split()))


for i in range(N):
  use_A=min(A,Price[i]//500)
  Price[i]-=use_A*500
  A-=use_A
  
  use_B=min(B,Price[i]//100)
  Price[i]-=use_B*100
  B-=use_B
  
  use_C=min(C,Price[i]//50)
  Price[i]-=use_C*50
  C-=use_C
  
  use_D=min(D,Price[i]//10)
  Price[i]-=use_D*10
  D-=use_D
  
  use_E=min(E,Price[i]//5)
  Price[i]-=use_E*5
  E-=use_E
  
  use_F=min(F,Price[i]//1)
  Price[i]-=use_F*1
  F-=use_F

if all([x == 0 for x in Price]):
  print("Yes")
else:
  print("No")
