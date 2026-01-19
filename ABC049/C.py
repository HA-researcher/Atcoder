S=list(input())
    #dream eraseがdreamerになってしまう
    #後ろから切り分けると安全
    #reversedして、<resare><esare><remaerd><maerd>なら、安全
    #そのはずが、erasereraser時にNoになる
    
S.reverse()
S="".join(S)

i=0
Flag=1
while Flag and i<len(S):
    if i+6<len(S):
        if S[i:i+7]=="remaerd":
            i+=7
            Flag=1
        else:
            Flag=0
    if i+5<len(S):
        if S[i:i+6]=="resare":
            i+=6
            Flag=1
        else:
            Flag=0
    if i+4<len(S):
        if S[i:i+5]=="maerd" or "esare":
            i+=5
            Flag=1
        else:
            Flag=0
    else:
        Flag=0
if Flag:
    print("YES")
else:
    print("NO")
