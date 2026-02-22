N,T=map(int,input().split())

A=list(map(int,input().split()))
A.append(T)

isOpen=1
nowTime=0
X_watch_time=0
for i in A:
    if i - nowTime>0:
        X_watch_time+=i - nowTime
        isOpen=0
        nowTime=i+100
            
print(X_watch_time)
