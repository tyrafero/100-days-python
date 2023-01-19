names= ["Raj","Vikram","Rolex","ashutosh","Shyam","Baburam"]
name_upper= []
for i in names:
    name_upper.append(i.upper())

for j in name_upper:  
    print(j+" Chauhan")

#################################################################################################
################################################################################################
student_heights = input("Enter the height of the student").split()

for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
    
# print(student_heights)

adder=0
n=0
for i in range(0,len(student_heights)):
    adder=adder+student_heights[i]
    n=n+1

mean= adder/n
print(mean)
########################################################################################


marks = input("enter studnets marks").split()

for i in range(0,len(marks)):
    marks[i] = int(marks[i])
    
hTemp=0
lTemp=0


for i in marks:
    if i>hTemp:
        hTemp=i
print(hTemp)        



# Sum oF all the even numbers from 1 to 100

total=0

for i in range(0,101):
    if i%2==0:
        total=total+i

print(total)
        
        
        
        


    