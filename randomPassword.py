#################################Password Generator###############################

alpha=[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# alpha=[]
# for i in Alpha:
#     alpha.append(i.lower())

# print(alpha)
import random

num=["0","1","2","3","4","5","6","7","8","9"]
sym=["!","@","#","$","%","^","&","*","(",")","-","+","="]

alpaN=int(input("Enter number of letters? "))
numN= int(input("Enter number of numbers? "))
symN= int(input("Enter number of symbols? "))
password=""
pas= random.choices(alpha,k=alpaN)+ random.choices(num,k=numN) + random.choices(sym,k=symN)
print(pas)
pw= random.sample(pas,len(pas))
print(pw)

# To List
password=""

for char in pw:
    password+=char

print(password)

# password= password + pw Concatenation Purposes
# print(password)