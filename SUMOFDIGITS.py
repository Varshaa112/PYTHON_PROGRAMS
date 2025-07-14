#pgm3
#program to find sum of digits
a=int(input("Enter any number"))
sum=0
while(a>0):
    sum=sum+a%10
    a=a//10
print("The sum of digits is ",sum)

#this code calculates the sum of digits of given num
#it repeatedly extracts the last digit using modulo operation and adds it to the sum
#then removes the last digit by performing interger division by 10 until the number becomes zero
#iter1 sum=0+3
# a=12
#iter2 sum=3+(12%10) = 3+2=5
# a=1
#iter3 sum= 5+1%10 = 6
# a=1//10
# a =0