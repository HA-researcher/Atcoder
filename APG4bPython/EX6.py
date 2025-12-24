A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)

if op == "-":
    print(A - B)
    
if op == "*":
    print(A * B)

if op == "/":
    if B!=0:
      print(int(A / B))
    else:
      print("error")

if op == "?":
    print("error")

if op == "=":
    print("error")

if op == "!":
    print("error")
