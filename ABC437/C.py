import sys
import numpy

input=sys.stdin.readline
T=int(input())

for i in range(T):
    N=int(input())
    WP=[]
    for j in range(N):
        WP.append(list(map(int,input().split())))
    WPNUM=numpy.array(WP)
    SUMW=numpy.sum(WPNUM[:,0])
    WP.sort(key=lambda x:x[0]+x[1],reverse=True)
    k=0
    while SUMW>0 and k<N:
        SUMW-=WP[k][0]+WP[k][1]
        k+=1
    if k==N:
        print(0)
    else:
        print(N-k)
