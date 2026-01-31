def OddOrEven(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"

def solve():
    a,b=map(int,input().split())
    if OddOrEven(a)=="Even" or OddOrEven(b)=="Even":
        print("Even")
    else:
        print("Odd")
if __name__ == "__main__":
    solve()
"""
#関数化
def OddOrEven(a,b):
    if a%2==0 or b%2==0:
        return "Even"
    else:
        return "Odd"

def solve():
    a,b=map(int,input().split())
    print(OddOrEven(a,b))
if __name__ == "__main__":
    solve()

"""
""”
a, b = map(int, input().split())
if a * b % 2:
    print("Odd")
else:
    print("Even")
"""
