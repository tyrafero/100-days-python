
print("Hungry Eye Pizza Shop")
print("---------------------------------------------------------------- \n")
print("Select Size")
print("---------------------------------------------------------------- \n")
size= input("Small Pizza $15 (press S) \nMedium Pizza $20 (press M) \nLarge Pizza $25 (press L) \n")
bill=0
if size=="S" :
    bill= 15
elif size=="M" :
    bill= 20
elif size=="L" :
    bill= 25
else :
    print("Invalid input, have a great day!")


topings= input("Extra Peppeoni topings. \n Small Pizza: +$2 (press S) \n Medium Pizza/ Large Pizza: +$3 (press M) \n No toppings: $0 (press Any key) \n")

if topings=="S":
    bill=bill+2
elif size=="M" or size=="L":
    bill=bill+3
else :
    print("You don't want Pepperoni toppings")
    
extra_cheese= input("Extra Cheese: +$1 \nPress Y or N \n ")
if extra_cheese=="Y":
    bill= bill+1
else:
    print("No Extra Cheese selected")

print("The final bill for the pizza is: " + str(bill))