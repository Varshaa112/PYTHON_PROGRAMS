#pgm2
#to find num is prime or not
a=int(input("Enter any number"))
c=0
for i in range(2,a):  #1 we cant consider as its factor of all so from 2 to a(the no we hv given)
    if(a%i==0):
        c=c+1
if(c==0):
    print("It is prime")
else:
    print("Not prime(composite)")