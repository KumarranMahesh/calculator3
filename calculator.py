# This calculator only adds and subtracts
a = int(input("Enter first number : "))
opr = int(input("Enter operator (+/-) : "))
b = int(input("Enter second number : "))

if opr == "+":
  print(f"The sum is : {a + b}")
elif opr == "-":
  print(f"The sum is : {a - b}")  
else:
  print("Invalid Input")
