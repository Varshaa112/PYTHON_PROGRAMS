a=int(input("enter number of rows"))
for i in range(a):
    for i in range(a-i):     #range(i+1) vice vers u get
        print("*",end=" ")
    print()
