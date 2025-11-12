'''
N=int(input())

count_=0
index_=1
for i in range(1,N+1):
  count2=0
  index2=i
  while i%2==0:
    i/=2
    count2+=1
  if count_<count2:
    count_=count2
    index_=index2
    
print(index_)
'''
'''
N=int(input())
if N==1:
  print("1")
  exit()

count_=0
calc_=1
while calc_<=N/2:
  calc_*=2
  count_+=1
  
print(calc_)
'''

N = int(input())

# N.bit_length() はNを2進数で表すのに必要な桁数を返す
# 例: N=7 (111) -> 3
# 例: N=8 (1000) -> 4
bit_len = N.bit_length()

# 答えは 2**(ビット長 - 1)
# 1 を (ビット長 - 1) 回左にシフトするのと同じ
ans = 1 << (bit_len - 1)

print(ans)
