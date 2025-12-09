#+(A-1)*N
import math

A,B=map(int,input().split())
"""
N=0
while B>1+(A-1)*N:
    N+=1
    """
N=math.ceil((B-1)/(A-1))

print(N)
