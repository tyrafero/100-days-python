

def primeChecker(n):
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
    if is_prime==True:
        print(f"The given number {n} is prime")
    else:
        print(f"The given number {n} is not prime")


#Method 2
primeChecker(int(input("Enter any number: ")))

n=int(input("Number"))
for i in range(2,n):
    if n%i==0:
        print(f"Its composite: {str(n)}")
        break
else:
    print(f"Its prime: {str(n)}")

        


# def greet():
#     print("Hello World")
#     print("Press")
#     print("Press again")


# greet()

# def SI(p,t,r):
#     interest= (p*t*r)/100
#     interest=int(interest)
#     print(interest)

# principal=int(input("enter p"))
# rate= int(input("enter rate"))
# time= int(input("enter time"))
# SI(principal,time,rate)
# n=input("enter any number to check:  ")