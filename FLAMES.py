b=input("Enter name of boy")
g=input("Enter girl name :)")
a1=list(b)
a2=list(g)

for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i]==a2[j]:
            a1[i]='2'
            a2[j]='2'

for i in a1:
    if i=='2':
        a1.remove(i)
for i in a2:
    if i=='2':
        a2.remove(i)


num=len(a1)+len(a2)
print(num)

ans=['FRIENDS','LOVE MARRIAGE','ARRANGE MARRIAGE','MADUVE','ENEMY','SIBLINGS']
index=0
while len(ans)!=1:
    index=(index+(num-1))%len(ans)
    ans.pop(index)
print("The relation is", ans[0])
