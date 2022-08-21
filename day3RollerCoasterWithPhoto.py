print("Welcome to World of Rollers")
print("_____________________________")

height= int(input("Enter your height: "))
bill=0

if height > 120:
    print("You can ride the roller coaster.")
    age= int(input("Enter your age: "))
    if age <= 18 and age >=12:
        bill=7
        print("Pay $7 at the counter")
    elif age <12:
        bill=5
        print("Pay $5 at the counter")
    else:
        bill=12
        print("Pay $12 at the counter")
    photo= input("Do you want your photo taken? \n Price of bill is $3. \n press y or n ")
    if photo=="y":
        bill= bill+3
        print("Pay "+str(bill)+" at the counter")
    
else:
    print("Sorry, you can't ride the roller.")

