N=int(input())

count_=0
index_=0
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
