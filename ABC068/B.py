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
