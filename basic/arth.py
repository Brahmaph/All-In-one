def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero is not allowed"
    
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

print("Add= ", add(num1,num2))
print("SUB= ", sub(num1,num2))
print("MUL= ", mul(num1,num2))
print("DIV= ", div(num1,num2))

