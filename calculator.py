def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Welcome to the calculator!")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == '+':
        print(f"Result: {add(x, y)}")
    elif operation == '-':
        print(f"Result: {subtract(x, y)}")
    elif operation == '*':
        print(f"Result: {multiply(x, y)}")
    elif operation == '/':
        print(f"Result: {divide(x, y)}")
    else:
        print("Invalid operation.")
