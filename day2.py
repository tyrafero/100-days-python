print("Welcome to the tip calculator \n")
totalBill= input("What was the total bill? \n")
noPeople= input("Enter number of people \n")

percentageTip= input("Percent of tip you like to give, 10|20|30 \n")

divideEach= float(totalBill)/int(noPeople)

totalPay= float(divideEach) + float(divideEach*(float(percentageTip)/100))

print("Each one of " +noPeople +" of you should pay \n" + str(totalPay))