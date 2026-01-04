N=int(input())
count=[0]*(N+1)
k=0
a_k=[]
for x in range(1,int((N/2)**(1/2)+2)):
    for y in range(x+1,int(N**(1/2)+2)):
        n=x**2+y**2
        if n>N:
            break
        count[n]+=1
for i in range(N+1):
    if count[i]==1:
        k+=1
        a_k.append(i)
print(k)
print(*a_k)
