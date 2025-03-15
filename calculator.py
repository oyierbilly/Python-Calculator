def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

    # Check if the result is a whole number
    if result == int(result):
        return int(result)  # Return as integer
    else:
        return result  # Return as float

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()