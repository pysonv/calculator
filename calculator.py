# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
    print("Simple Calculator")
    print("------------------")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        op = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        op = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        op = "*"
    elif choice == '4':
        result = divide(num1, num2)
        op = "/"
    else:
        print("Invalid operation choice.")
        return

    print(f"\nResult: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
