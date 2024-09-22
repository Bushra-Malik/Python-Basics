# Get user input for operation
operation = input("Enter operation (+, -, *, /): ")

# Get user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error! Division by zero is not allowed.")
        result = None
else:
    print("Error! Invalid operation.")
    result = None

# Print result
if result is not None:
    print("Result: ", result)