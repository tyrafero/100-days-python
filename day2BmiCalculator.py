weight= input("Please enter your weight in Kg \n")
height = input("Please enter your height in Cm \n")

bmi= (float(weight)/(float(height)**2))*10000   #converting cm to metre

print("Your BMI is " + str(bmi))