#counting number of words in the sentence
import time

str1=input("Enter a sentence")
b=0
for i in range(len(str1)): #checking for len of str1
    if(str1[i]==" " and str1[i+1]!= " "):
        b=b+1
time.sleep(2)
print("The words are",b+1)
