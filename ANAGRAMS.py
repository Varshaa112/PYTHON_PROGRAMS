#sorted string if they are same then they are anagrams
#dog= dgo
#god=dgo

str1=input("Enter string1")
str2=input("Enter string2")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i!=" ") #removing white spaces in a
b1="".join(i for i in b if i!=" ") #removing white spaces in b
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("It is anagram")
else:
    print("not anagram")
