N,X=map(int,(input().split()))
A=list(map(int,input().split()))

for i in A:
    if i<X:
        X=i
        print("1")
    else:
        print("0")
