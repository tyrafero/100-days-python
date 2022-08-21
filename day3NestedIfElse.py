print("Welcome to World of Rollers")
print("_____________________________")

height= int(input("Enter your height: "))


if height > 120:
    print("You can ride the roller coaster.")
    age= int(input("Enter your age: "))
    if age <= 18 and age >=12:
        print("Pay $7 at the counter")
    elif age <12:
        print("Pay $5 at the counter")
    else:
        print("Pay $12 at the counter")
else:
    print("Sorry, you can't ride the roller.")