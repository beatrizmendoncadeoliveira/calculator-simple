def simple_calculator():
    print("Welcome to the Simple Calculator!")
    print("This calculator can perform addition, subtraction, multiplication, and division.")
    print("It supports both whole numbers and decimal numbers.")
    
    try:
        # Input the first number
        num1 = float(input("Enter the first number: "))
        
        # Input the second number
        num2 = float(input("Enter the second number: "))
        
        # Ask the user for the operation
        operation = input("Choose the operation (enter '+' for addition, '-' for subtraction, '*' for multiplication, or '/' for division): ").strip()
        
        # Perform the selected operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} plus {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} minus {num2} is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} multiplied by {num2} is: {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"The result of {num1} divided by {num2} is: {result}")
        else:
            print("Invalid operation! Please enter '+', '-', '*', or '/'.")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
simple_calculator()
