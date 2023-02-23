import random

friends = "Hema, Rekha, Jaya, Sushma, Nirma"
op_friends = friends.split(",")

print(op_friends)

print("\nWelcome to London Pub \n")

print("Who pays the bill? \n")

choice_person = random.choice(op_friends)

print(f"{choice_person} pays the bill")