from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

#PAUSE 1
# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# PAUSE 2
# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

functions = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

# PAUSE 3
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.

# answer = 0.0

def user_input(num_1, num_2, op):
    num_1 = float(input("What's the first number?: "))
    for operation in functions:
        print(functions[operation])
    op = input("Pick an operation: ")
    num_2 = float(input("What's the next number?: "))

    return (num_1, num_2, op)

def calculator_output(first_number, second_number, user_operation):
    global answer
    if user_operation == "+":
        answer = add(first_number, second_number)
        print(f"{first_number} + {second_number} = {answer}")
    elif user_operation == "-":
        answer = subtract(first_number, second_number)
        print(f"{first_number} - {second_number} = {answer}")
    elif user_operation == "*":
        answer = multiply(first_number, second_number)
        print(f"{first_number} * {second_number} = {answer}")
    elif user_operation == "/":
        answer = divide(first_number, second_number)
        print(f"{first_number} / {second_number} = {answer}")

    return answer

def calculate():
    for operation in functions:
        print(functions[operation])
    op = input("Pick an operation: ")
    num_2 = float(input("What's the next number?: "))

    calculator_output(num_1, num_2, op)
    user_calc()


def user_calc():
    global num_1
    user_option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

    if user_option == "y":
        num_1 = answer
        calculate()
    elif user_option == "n":
        num_1 = float(input("What's the first number?: "))
        calculate()

    return num_1

num_1 = float(input("What's the first number?: "))
calculate()