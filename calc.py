import json
import os

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

def simple_calculator():
    print("Welcome to the Advanced Simple Calculator!")
    print("This calculator can perform addition, subtraction, multiplication, and division.")
    print("It supports both whole numbers, decimal numbers, and variable substitution.")
    print("Type 'exit' to quit.")
    
    # Load variables from cache
    variables = load_cache()
    
    while True:
        try:
            # Input the expression or command
            user_input = input("Enter an expression (e.g., 'x = 10', 'x + 5', or 'exit' to quit): ").strip()
            
            # Exit the calculator
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                save_cache(variables)  # Save variables to cache before exiting
                break
            
            # Handle variable assignment (e.g., "x = 10")
            if '=' in user_input:
                var_name, value = user_input.split('=', 1)
                var_name = var_name.strip()
                value = value.strip()
                
                try:
                    # Evaluate the value (e.g., "x = 5 + 3")
                    value = eval(value, {}, variables)
                    variables[var_name] = value
                    print(f"Variable '{var_name}' set to {value}.")
                    
                    # Log the activity
                    log_activity({
                        "type": "variable_assignment",
                        "variable": var_name,
                        "value": value,
                        "expression": user_input
                    })
                except Exception as e:
                    print(f"Error: Invalid expression. {e}")
                continue
            
            # Evaluate the expression (e.g., "x + 5")
            try:
                result = eval(user_input, {}, variables)
                print(f"The result is: {result}")
                
                # Log the activity
                log_activity({
                    "type": "calculation",
                    "expression": user_input,
                    "result": result
                })
            except Exception as e:
                print(f"Error: Invalid expression. {e}")
        
        except KeyboardInterrupt:
            print("\nExiting the calculator. Goodbye!")
            save_cache(variables)  # Save variables to cache before exiting
            break

# Run the calculator
simple_calculator()
