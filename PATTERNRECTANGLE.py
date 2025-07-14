#**********
#*        *
#*        *
#*        *
#**********

# Hollow square of stars (*)

n = int(input("Enter the size of the square: "))

for i in range(n): #row
    for j in range(n): #col
        # Print * only for the border positions
        if i == 0 or i == n-1 or j == 0 or j == n-1: #0->top row i->n-1 bottom row j->0 first column j=n-1-> last column
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

