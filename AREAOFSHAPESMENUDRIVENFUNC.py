#MENU DRIVEN PROGRAM TO FIND AREA OF CIRCLE, SQUARE, TRIANGLE, RECTANGLE
# for switch in python a=11 match a: case 10: print("Super") case 20: print("BLAh") case _: print("LSMDM")

def circle():
    radius=int(input("Enter radius of circle "))
    areaofcircle= 3.14*radius*radius
    print("Area of circle is:", areaofcircle)

def square(a):
    side=int(input("Enter side of square"))
    areaofsquare=side*side
    print("Area of square", areaofsquare)

def triangle():
    base = int(input("Enter base of triangle"))
    height = int(input("Enter height of triangle"))
    return 0.5*base*height

def rectangle(a,b):

    return length*breadth


while(True):
    choice = int(input("Enter your choice"))
    match choice:
            case 1:
                circle()
            case 2:
                square()
            case 3:
                res=triangle()
                print("Area of triangle",res)
            case 4:
                length = int(input("Enter length of rectangle"))
                breadth = int(input("Enter breadth of rectangle"))
                res=rectangle(length,breadth)
                print("Area of rectangle",res)
            case 5:
                exit()
            case _:
                print("Invalid choiceEnter number from 1-4")

