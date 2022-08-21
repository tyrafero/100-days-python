print("Welcome to your own BMI Calculator.")
print("____________________________________")

weight= input("Please enter your weight in Kg \n")
height = input("Please enter your height in Cm \n")

bmi= (float(weight)/(float(height)**2))*10000   #converting cm to metre
bmi= round(bmi,2)
print("Your BMI is " + str(bmi))


if bmi< 18.5:
    print("Your BMI is: " + str(bmi) +". You are underweight.")
elif bmi> 18.5 and bmi< 25:
    print("Your BMI is: " + str(bmi) +". You have a normal weight.")
elif bmi> 25 and bmi< 30:
    print("Your BMI is: " + str(bmi) +". You are overweight.")
elif bmi> 30 and bmi<35:
    print("Your BMI is: " + str(bmi) +". You are obese.")
else:
    print("Your BMI is: " + str(bmi) +". You are clinically obese")
