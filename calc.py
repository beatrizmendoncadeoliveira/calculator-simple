def multiplication_calculator():
    print("Welcome to the Simple Multiplication Calculator!")
    
    try:
        # Input the first number
        num1 = float(input("Enter the first number: "))
        
        # Input the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform multiplication
        result = num1 * num2
        
        # Display the result
        print(f"The result of {num1} multiplied by {num2} is: {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
multiplication_calculator()
