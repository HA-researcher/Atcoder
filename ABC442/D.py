N,Q=map(int,input().split())

#いもす法の総和とりたいけど、それだけじゃ入れ替えのせいでぐちゃぐちゃ？
#いれかえのたびに総和に変化する？左右入れ替えだけなので、
#たとえば総和の列が0,4,8,11,19で[2],[3]入れ替えなら、(列は4,4,3,8)
#list[2]=list[2]+list[3]-list[2]-list[2]+list[1]
#list[2]=list[3]-list[2]+list[1]
#8+(11-8)-(8-4)

A=list(map(int,input().split()))
sumslist=[0]
for i in range(len(A)):
    sumslist.append(sumslist[i]+A[i])
    
for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        sumslist[query[1]]=sumslist[query[1]+1]-sumslist[query[1]]+sumslist[query[1]-1]

        #print(sumslist)

    elif query[0]==2:
        print(sumslist[query[2]]-sumslist[query[1]-1])
        #print(sumslist)




