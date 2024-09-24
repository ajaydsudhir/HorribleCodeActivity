# function to multiply two numbers
def add(a, b):
    return a + b


# function to subtract two numbers
def subtract(a, b):
    return a - b


# function to multiply two numbers
def multiply(a, b):
    return a * b


# function to divide two numbers
def divide(a, b):
    return a / b


def main():
    while True:
        print("Choose operation: add, subtract, multiply, or divide: ")
        operation = input()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == 'add':
            print("Result:", add(num1, num2))
        elif operation == 'subtract':
            print("Result:", subtract(num1, num2))
        elif operation == 'multiply':
            print("Result:", multiply(num1, num2))
        elif operation == 'divide':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation!")

        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() != 'yes':
            break


main()
