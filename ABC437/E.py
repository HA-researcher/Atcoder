##うまくいかない
N=int(input())
XY=[]
for i in range(N):
    X,Y=map(int,input().split())
    if X!=0:
        X=XY[X-1][0]
    else:
        X=Y
        Y=0
    XY.append([X,Y,i+1])
XY.sort(key=lambda x:(x[0],x[0]+x[1],x[2]),reverse=False)
for i in range(N):

    print(XY[i][2],end=" ")
