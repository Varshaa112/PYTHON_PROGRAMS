#factors of 100
a=int(input("Enter number"))
for i in range(2,a):
    if(a%i==0):
        print("factor of ",a, "is", i)