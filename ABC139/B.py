#+(A-1)*N
"""
import math
"""
A,B=map(int,input().split())
"""
N=0
while B>1+(A-1)*N:
    N+=1
N=math.ceil((B-1)/(A-1))
"""
#X/Yの切り上げ演算、(X+Y-1)//Y
N=(B-1+A-1-1)//(A-1)
print(N)
