
def addition(first_number, second_number, operation):
    return f"{first_number} {operation} {second_number} = {first_number + second_number}"

def subtraction(first_number, second_number, operation):
    return f"{first_number} {operation} {second_number} = {first_number - second_number}"

def multiplication(first_number, second_number, operation):
    return f"{first_number} {operation} {second_number} = {first_number * second_number}"

def division(first_number, second_number, operation):
    if second_number == 0:
        return "Error: Division by zero"
    return f"{first_number} {operation} {second_number} = {first_number / second_number}"

def calculator():
    first_number = int(input("What's the first nuber? "))
    second_number = int(input("What's the second nuber? "))
    valid_operator = False
    while not valid_operator:
        operation = input("Pick an operation:\n+\n-\n*\n/\n")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            valid_operator = True
            if operation == "+":
                result = addition(first_number, second_number, operation)
            elif operation == "-":
                result = subtraction(first_number, second_number, operation)
            elif operation == "*":
                result = multiplication(first_number, second_number, operation)
            else:
                result = division(first_number, second_number, operation)
            print(result)
        else:
            print("Not a valid operator")
calculator()

