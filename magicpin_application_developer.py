password=list(raw_input().strip().split(','))
for p in password:
    special=["*","$","_","#","=","@"]
    non=["%","!","(",")"]
    f1=0
    f2=0
    f3=0
    f4=0
    f5=0
    if len(p)<6:
        print p,"Failure Password must be at least 6 characters long."
        continue
    if len(p)>12:
        print p,"Failure Password must be at max 12 characters long."
        continue
    for i in p:
        if i>=chr(65) and i<=chr(90):
            f3+=1
        elif i>=chr(97) and i<=chr(122):
            f1+=1
        elif i>=chr(48) and i<=chr(57):
            f2+=1
        elif i in special:
            f4+=1
        elif i in non:
            f5+=1
            break
    if f1==0:
        print p,"Failure Password must contain at least one letter from a-z."
    elif f2==0:
        print p,"Failure Password must contain at least one letter from 0-9."
    elif f3==0:
        print p,"Failure Password must contain at least one letter from A-Z."
    elif f4==0:
        print p,"Failure Password must contain at least one letter from *$_#=@."
    elif f5!=0:
        print p,"Failure Password cannot contain %!)(."
    else:
        print p,"Success"

