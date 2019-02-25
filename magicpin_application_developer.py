password=list(raw_input().strip().split(','))
#print password
for p in password:
    special=["*","$","_","#","=","@"]
    non=["%","!","(",")"]
    f=[0]*5
    if len(p)<6:
        print p,"Failure Password must be at least 6 characters long."
        continue
    if len(p)>12:
        print p,"Failure Password must be at max 12 characters long."
        continue
    for i in p:
        if i>=chr(65) and i<=chr(90):
            f[2]+=1
        elif i>=chr(97) and i<=chr(122):
            f[0]+=1
        elif i>=chr(48) and i<=chr(57):
            f[1]+=1
        elif i in special:
            f[3]+=1
        elif i in non:
            f[4]+=1
            break
    if f[0]==0:
        print p,"Failure Password must contain at least one letter from a-z."
    elif f[1]==0:
        print p,"Failure Password must contain at least one letter from 0-9."
    elif f[2]==0:
        print p,"Failure Password must contain at least one letter from A-Z."
    elif f[3]==0:
        print p,"Failure Password must contain at least one letter from *$_#=@."
    elif f[4]!=0:
        print p,"Failure Password cannot contain %!)(."
    else:
        print p,"Success"

