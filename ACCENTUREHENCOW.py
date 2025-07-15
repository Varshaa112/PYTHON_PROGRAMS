#print no of hens and cows
#cows num of legs 4 heads 1
#hens num of legs 2 heads 1
heads=int(input("Enter the number of heads"))
legs=int(input("Enter the number of legs"))
flag=False
for hen in range(heads):
    cow=heads-hen
    if cow*4 + hen*2 == legs:
        print("COWS: ", cow)
        print("HENS:", hen)
        flag=True
        break
if not flag:
    print("no solution")
