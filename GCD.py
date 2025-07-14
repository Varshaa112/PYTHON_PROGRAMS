#euclidean algorithm
#gcd of 2 numbers
#greattest common divisor
a=int(input("Enter num1"))
b=int(input("Enter num2"))
c=0
while b!= 0: #we dono number of iterations so we choose while loop
    c= a % b #storing
    a=b
    b=c
print("GCD ",a)


