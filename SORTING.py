#SORTING THE EVEN NUMBERS ODD NUMBERS AND STRING IN ASCENDING
a=[10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
a1=[]
a2=[]
a3=[]

for i in a:
    if type(i) == str:  #this must be first condn str then int if str is last it wont take or give output
        a3.append(i)
    elif i%2==0:
        a1.append(i)
    elif i%2!=0:
        a2.append(i)
    a1.sort()
    a2.sort()
    a3.sort()
print(a1+a2+a3)
