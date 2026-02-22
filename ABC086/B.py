a, b = map(int, input().split())
f = (a*10 ** (len(str(b))) + b) ** (1 / 2)
if f.is_integer():
    print("Yes")
else:
    print("No")
