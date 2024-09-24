def calculate(operation, num1, num2):
    if operation == 'add':
        print("Result:", num1 + num2)
    elif operation == 'subtract':
        print("Result:", num1 - num2)
    elif operation == 'multiply':
        print("Result:", num1 * num2)
    elif operation == 'divide':
        print("Result:", num1 / num2)
    else:
        print("Wrong input")

print("Choose operation (add, subtract, multiply, divide) :")
operation = input()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculate(operation, num1, num2)

print("Choose operation (add, subtract, multiply, divide) :")
operation2 = input()
num3 = float(input("Enter first number: "))
num4 = float(input("Enter second number: "))
calculate(operation2, num3, num4)

print("Choose operation (add, subtract, multiply, divide) :")
operation3 = input()
num5 = float(input("Enter first number: "))
num6 = float(input("Enter second number: "))
calculate(operation3, num5, num6)
