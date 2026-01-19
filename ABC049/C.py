#52分から　目標9分 17分時点でテストコードACなものの、erasereraser時の切り分け失敗

S=input()
lenS=len(S)

i=0
Flag=1
while Flag and i<lenS:
    if i+6<lenS:
        if S[i:i+7]=="dreamer":
            i+=7
            Flag=1
        else:
            Flag=0
            
        
    if i+5<lenS:
        if S[i:i+6]=="eraser":
            i+=6
            Flag=1
        else:
            Flag=0
    
    if i+4<lenS:
        if S[i:i+5]=="dream" or "erase":
            i+=5
            Flag=1
        else:
            Flag=0
    else:
        Flag=0
if Flag:
    print("YES")
else:
    i=0
    Flag=1
    while Flag and i<lenS:
        if i+4<lenS:
            if S[i:i+5]=="dream" or "erase":
                i+=5
                Flag=1
            else:
                Flag=0
        else:
            Flag=0
        if i+6<lenS:
            if S[i:i+7]=="dreamer":
                i+=7
                Flag=1
            else:
                Flag=0
                
        
        if i+5<lenS:
            if S[i:i+6]=="eraser":
                i+=6
                Flag=1
            else:
                Flag=0
    if Flag:
        print("YES")
    else:
        print("NO")
