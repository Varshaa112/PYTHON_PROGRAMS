n = int(input("Enter the no of teams"))
teams=[]
for i in range(n):
    a=input("Enter the name of the teams")
    teams.append(a)
meet=int(input("ENter no of meeting of btw 1 pairs "))

match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])

print("----------")
index=1
for i in match:
    print("Match {}: {} {}".format(index,i[0],i[1]))
    index=index+1



