import string


print("Welcome to graha-jotishi")

name1= input("What is your name? \n")
name2= input("What is their name name? \n")

t= name1.count("t") + name2.count("t")
r= name1.count("r") + name2.count("r")
u= name1.count("u") + name2.count("u")
e= name1.count("e") + name2.count("e")

l= name1.count("l") + name2.count("l")
o= name1.count("o") + name2.count("o")
v= name1.count("v") + name2.count("v")
e= name1.count("e") + name2.count("e")

true= t+r+u+e
love=l+o+v+e


loveP= str(true) + str(love)
str(loveP)
print("Love percentage of "+name1+ " and " +name2 +" is "  + str(loveP))
