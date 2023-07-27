import sys
def addition(num1, num2):
    num1 += num2
    return num1
def subtraction(num1, num2):
    num1 -= num2
    return num1
def multiplication(num1, num2):
    num1 *= num2
    return num1
def division(num1, num2):
    num1 /= num2
    return num1
def module(num1, num2):
    num1 %= num2
    return num1
switcher = {
    1:addition,
    2:subtraction,
    3:multiplication,
    4:division,
    5:module
}
def switch (operation, num1, num2) :

    return switcher.get(operation)(num1,num2)
    
print("""You can perform operation:
1:Addition
2:Subtraction
3:Multiplication
4:Division
5:Module
""")

choice = int(input("Select operation: "))
if choice <0 or choice > 5:
    print("Invalid Operation")
    sys.exit(0)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
val=switch(choice,num1,num2)
print(val)

