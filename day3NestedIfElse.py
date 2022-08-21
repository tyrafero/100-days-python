height= int(input("Enter your height: "))
age= int(input("Enter your age: "))

if height > 120:
    print("You can ride the roller coaster.")
    
    if age > 18:
        print("Pay $12 at the counter")
    else:
        print("Pay $7 at the counter")
else:
    print("Sorry, you can't ride the roller.")