S = input()
# ここにプログラムを追記
total=1
for i in range(1,len(S)):
 if S[i-1]=="+":
  total+=int(S[i])
 elif S[i-1]=="-":
  total-=int(S[i])
print(total)
