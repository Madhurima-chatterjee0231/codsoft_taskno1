print("Simple Calculator")
num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
print("Press 1 for Addition\nPress 2 for Substraction\nPress 3 for Multiplication\nPress 4 for Division")
choice=int(input("Enter your choice from 1-4:"))
if choice ==1:
    print("Addition of given two numbers are:", num1+num2)
elif choice ==2:
    print("Substraction of given two numbers are:", num1-num2)
elif choice ==3:
    print("Multiplication of given two numbers are:" ,num1*num2)
elif choice ==4:
    print("Division of two numbers are:", num1/num2)
else:
    print("Invalid Input")


