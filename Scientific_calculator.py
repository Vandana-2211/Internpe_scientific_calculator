import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Main calculator loop
while True:
    print("Scientific Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("0. Exit")

    choice = input("Enter your choice (0-10): ")

    if choice == '0':
        print("Exiting the calculator...")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))

    elif choice == '3':
        print("Result:", multiply(num1, num2))

    elif choice == '4':
        print("Result:", divide(num1, num2))

    elif choice == '5':
        print("Result:", power(num1, num2))

    elif choice == '6':
        num = float(input("Enter a number: "))
        print("Result:", square_root(num))

    elif choice == '7':
        num = float(input("Enter a number: "))
        base = float(input("Enter the base (default is 10): "))
        print("Result:", logarithm(num, base))

    elif choice == '8':
        num = float(input("Enter an angle in degrees: "))
        print("Result:", sin(num))

    elif choice == '9':
        num = float(input("Enter an angle in degrees: "))
        print("Result:", cos(num))

    elif choice == '10':
        num = float(input("Enter an angle in degrees: "))
        print("Result:", tan(num))

    else:
        print("Invalid input. Please enter a valid option.")
