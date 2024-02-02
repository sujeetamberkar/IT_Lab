def simple_calculator():
    # Displaying operation choices
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Taking input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Checking if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            # Checking if the second number is not zero for division
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Cannot divide by zero!")

    else:
        print("Invalid Input")

# To run the calculator, just call simple_calculator()
# simple_calculator()  # Uncomment this line to run the calculator
simple_calculator()