import math
h=int(input("Enter height: "))
w=int(input("Enter width: "))

def areaCalc(height,width):
    Area= height*width
    return Area

Area= areaCalc(h,w)

def paintCalc(a):
    paint= math.ceil(a/5)
    print(f"You need {paint} number of cans. ")
    
paintCalc(Area)