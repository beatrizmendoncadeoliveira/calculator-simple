# Advanced Simple Calculator

This is an advanced simple calculator written in Python. It supports basic arithmetic operations (addition, subtraction, multiplication, and division), variable substitution, activity logging, and caching.

## Features

- **Basic Operations**: Perform addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Variable Substitution**: Store values in variables and use them in calculations.
- **Decimal Numbers**: Supports both whole and decimal numbers.
- **Activity Logging**: Logs all activities (variable assignments and calculations) in a JSON file (`activity.json`).
- **Caching**: Saves the current state of variables to a `cache.txt` file for persistence.

## How to Use

1. **Run the Script**:
   - Make sure you have Python installed on your system.
   - Download or clone the script to your local machine.
   - Open a terminal or command prompt and navigate to the directory containing the script.
   - Run the script using the following command:
     ```bash
     python calculator.py
     ```

2. **Using the Calculator**:
   - The calculator supports the following commands:
     - **Variable Assignment**: Assign a value to a variable (e.g., `x = 10`).
     - **Calculations**: Perform calculations using numbers or variables (e.g., `x + 5`).
     - **Exit**: Type `exit` to quit the calculator.

3. **Examples**:
   - Assign a value to a variable:
     ```
     Enter an expression (e.g., 'x = 10', 'x + 5', or 'exit' to quit): x = 10
     Variable 'x' set to 10.
     ```
   - Perform a calculation:
     ```
     Enter an expression (e.g., 'x = 10', 'x + 5', or 'exit' to quit): x + 5
     The result is: 15
     ```
   - Use variables in calculations:
     ```
     Enter an expression (e.g., 'x = 10', 'x + 5', or 'exit' to quit): y = x * 2
     Variable 'y' set to 20.
     ```
   - Exit the calculator:
     ```
     Enter an expression (e.g., 'x = 10', 'x + 5', or 'exit' to quit): exit
     Exiting the calculator. Goodbye!
     ```

4. **Activity Logging**:
   - All activities (variable assignments and calculations) are logged in a JSON file (`activity.json`).
   - Example `activity.json`:
     ```json
     [
         {
             "type": "variable_assignment",
             "variable": "x",
             "value": 10,
             "expression": "x = 10"
         },
         {
             "type": "calculation",
             "expression": "x + 5",
             "result": 15
         }
     ]
     ```

5. **Caching**:
   - The current state of variables is saved to a `cache.txt` file when the program exits.
   - Example `cache.txt`:
     ```json
     {"x": 10, "y": 20}
     ```

## Requirements

- Python 3.x

## Files

- `calculator.py`: The main script for the calculator.
- `activity.json`: Logs all activities (automatically created by the script).
- `cache.txt`: Stores the current state of variables (automatically created by the script).

## License

This project is open-source and available under the MIT License.

---

Enjoy using the Advanced Simple Calculator! If you have any questions or suggestions, feel free to open an issue or contribute to the project.
