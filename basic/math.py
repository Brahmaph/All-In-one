num1 = float(input("Enter 1st num: "))
num2 = float(input("Enter 2nd num: "))

operator = input("Select +,-,*,/ ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Invalid operator")