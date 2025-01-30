import json
import os
from fractions import Fraction

# File paths
ACTIVITY_LOG_FILE = "activity.json"
CACHE_FILE = "cache.txt"

def load_cache():
    """Load variables from the cache file if it exists."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_cache(variables):
    """Save variables to the cache file."""
    with open(CACHE_FILE, "w") as file:
        json.dump(variables, file)

def log_activity(activity):
    """Log activities to a JSON file."""
    if not os.path.exists(ACTIVITY_LOG_FILE):
        with open(ACTIVITY_LOG_FILE, "w") as file:
            json.dump([], file)
    
    with open(ACTIVITY_LOG_FILE, "r") as file:
        activities = json.load(file)
    
    activities.append(activity)
    
    with open(ACTIVITY_LOG_FILE, "w") as file:
        json.dump(activities, file, indent=4)

def mixed_division(result):
    """
    Convert a decimal result to mixed division format (e.g., 2.5 -> 2 1/2).
    """
    if isinstance(result, float) and not result.is_integer():
        # Convert to fraction
        frac = Fraction(result).limit_denominator()
        whole = frac.numerator // frac.denominator
        remainder = frac.numerator % frac.denominator
        
        if whole == 0:
            return f"{remainder}/{frac.denominator}"
        else:
            return f"{whole} {remainder}/{frac.denominator}"
    else:
        return str(result)

def show_menu():
    """Display the calculator menu."""
    print("\n--- Calculator Menu ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Mixed Division (e.g., 2 1/2)")
    print("6. Exit")
    choice = input("Choose an operation (1-6): ").strip()
    return choice

def simple_calculator():
    print("Welcome to the Advanced Simple Calculator!")
    print("This calculator can perform addition, subtraction, multiplication, and division.")
    print("It supports both whole numbers, decimal numbers, and variable substitution.")
    
    # Load variables from cache
    variables = load_cache()
    
    while True:
        choice = show_menu()
        
        # Exit the calculator
        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            save_cache(variables)  # Save variables to cache before exiting
            break
        
        # Input the expression based on the chosen operation
        if choice in ['1', '2', '3', '4', '5']:
            try:
                # Input the first number or variable
                num1 = input("Enter the first number or variable: ").strip()
                if num1 in variables:
                    num1 = variables[num1]
                else:
                    num1 = float(num1)
                
                # Input the second number or variable
                num2 = input("Enter the second number or variable: ").strip()
                if num2 in variables:
                    num2 = variables[num2]
                else:
                    num2 = float(num2)
                
                # Perform the chosen operation
                if choice == '1':
                    result = num1 + num2
                    operation = "+"
                elif choice == '2':
                    result = num1 - num2
                    operation = "-"
                elif choice == '3':
                    result = num1 * num2
                    operation = "*"
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    result = num1 / num2
                    operation = "/"
                elif choice == '5':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    result = num1 / num2
                    operation = "/"
                    mixed_result = mixed_division(result)
                    print(f"Mixed division result: {mixed_result}")
                
                # Display the result
                print(f"The result of {num1} {operation} {num2} is: {result}")
                
                # Log the activity
                log_activity({
                    "type": "calculation",
                    "operation": operation,
                    "num1": num1,
                    "num2": num2,
                    "result": result,
                    "mixed_result": mixed_result if choice == '5' else None
                })
            except ValueError:
                print("Error: Invalid input! Please enter numeric values.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice! Please choose a valid option (1-6).")

# Run the calculator
simple_calculator()
