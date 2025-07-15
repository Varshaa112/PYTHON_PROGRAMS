#enter no of blocks :3
#enter no of lines :4
#enter no of stars :5
#-------------BLOCK1-------------
#* * * * *
#* * * * *
#* * * * *
#* * * * *

a=int(input("Enter no of blocks"))
b=int(input("Enter no of lines"))
c=int(input("Enter no stars"))
sum=0
for i in range(a):
    print("----------BLOCK",i+1,"--------------")
    count=0 #for counting stars of each block
    line=b-i #to reduce the number of lines in each block
    if line<=0:
        continue
    for i in range(line):
        for j in range(c):
            print("*",end=" ")
            count=count+1

        print()
    print(count)
    sum+=count #adds each block count
print("Total stars",sum)