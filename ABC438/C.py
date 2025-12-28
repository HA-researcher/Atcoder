N=int(input())
A=list(map(int,input().split()))

stack=[]
for x in A:
    stack.append(x)
    if len(stack)>3:
        if stack[-4]==stack[-3]==stack[-2]==stack[-1]:
            for _ in range(4):
                stack.pop()
print(len(stack))
