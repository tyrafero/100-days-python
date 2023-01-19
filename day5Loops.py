# names= ["Raj","Vikram","Rolex","ashutosh","Shyam","Baburam"]
# name_upper= []
# for i in names:
#     name_upper.append(i.upper())

# for j in name_upper:  
#     print(j+" Chauhan")

#################################################################################################
################################################################################################
# student_heights = input("Enter the height of the student").split()

# for i in range(0,len(student_heights)):
#     student_heights[i] = int(student_heights[i])
    
# # print(student_heights)

# adder=0
# n=0
# for i in range(0,len(student_heights)):
#     adder=adder+student_heights[i]
#     n=n+1

# mean= adder/n
# print(mean)
########################################################################################


# marks = input("enter studnets marks").split()
# 12

# for i in range(0,len(marks)):
#     marks[i] = int(marks[i])
    
# hTemp=0
# lTemp=0


# for i in marks:
#     if i>hTemp:
#         hTemp=i
# print(hTemp)        



# Sum oF all the even numbers from 1 to 100

# total=0

# for i in range(0,101):
#     if i%2==0:
#         total=total+i

# print(total)
        
        
        
        
###################################FiZZ BUzz game################################################################

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

    

#################################Password Generator###############################

alpha=[ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# alpha=[]
# for i in Alpha:
#     alpha.append(i.lower())

# print(alpha)
import random

num=["0","1","2","3","4","5","6","7","8","9"]
sym=["!","@","#","$","%","^","&","*","(",")","-","+","="]

alpaN=4
numN=2
symN=2
password=""
pas= random.choices(alpha,k=alpaN)+ random.choices(num,k=numN) + random.choices(sym,k=symN)
print(pas)
print(random.sample(pas,len(pas)))

# password= password + pw Concatenation Purposes
# print(password)
