a=int(input("Enter num1"))
b=int(input("Enter num2"))
c=int(input("Enter num3"))
if(a>=b and a<=c):
    print("second largest number is",a)
elif(b>=a and b<=c):
    print("second largest number is",b)
else:
    print("second largest number is",c)
