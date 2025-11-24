print("=== Simple Calculator ===")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (+, -, *, /): ")

    if choice == '+':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '-':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '*':
        print(f"Result: {num1} × {num2} = {num1 * num2}")
    elif choice == '/':
        if num2 != 0:
            print(f"Result: {num1} ÷ {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice!")

    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator!")
        break
