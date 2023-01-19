# names= ["Raj","Vikram","Rolex","ashutosh","Shyam","Baburam"]
# name_upper= []
# for i in names:
#     name_upper.append(i.upper())

# for j in name_upper:  
#     print(j+" Chauhan")


student_heights = input("Enter the height of the student").split()

for i in range(0,len(student_heights)):
    student_heights[i] = int(student_heights[i])
    
# print(student_heights)

adder=0

for i in range(0,len(student_heights)):
    adder=adder+student_heights[i]

mean= adder/len(student_heights)
print(mean)
    