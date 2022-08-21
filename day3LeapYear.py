year= int(input("Enter year that you want to check \t"))

if year%4 == 0 and year%100 !=0:
    print("The entered year " +str(year)+ "  is a leap year")
    
elif year%100 ==0 and year%400==0:
    print("The entered year " +str(year)+ "  is a leap year")

else:
    print("The entered year " +str(year)+ " is not a leap year")
