#program of strong password
#Level 1

s=input("Enter password")
dg=0
up=0
lw=0
sp=0
if(len(s)>7):
    for i in s:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lw=lw+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    if(dg>0 and up>0 and lw>0 and sp>0):
        print("Strong password")
    else:
        print("Password is weak")
else:
    print("Length of password should be 8 character minimum")
