const fs = require('fs');

// File paths
const ACTIVITY_LOG_FILE = "activity.json";
const CACHE_FILE = "cache.txt";

// Load variables from the cache file if it exists
function loadCache() {
    if (fs.existsSync(CACHE_FILE)) {
        const data = fs.readFileSync(CACHE_FILE, 'utf8');
        return JSON.parse(data);
    }
    return {};
}

// Save variables to the cache file
function saveCache(variables) {
    fs.writeFileSync(CACHE_FILE, JSON.stringify(variables), 'utf8');
}

// Log activities to a JSON file
function logActivity(activity) {
    let activities = [];
    if (fs.existsSync(ACTIVITY_LOG_FILE)) {
        const data = fs.readFileSync(ACTIVITY_LOG_FILE, 'utf8');
        activities = JSON.parse(data);
    }
    activities.push(activity);
    fs.writeFileSync(ACTIVITY_LOG_FILE, JSON.stringify(activities, null, 4), 'utf8');
}

// Convert a decimal result to mixed division format (e.g., 2.5 -> 2 1/2)
function mixedDivision(result) {
    if (Number.isInteger(result)) {
        return result.toString();
    }

    const tolerance = 1.0e-6; // Tolerance for floating-point comparison
    let whole = Math.floor(result);
    let remainder = result - whole;

    // Find the nearest fraction
    for (let denominator = 1; denominator <= 100; denominator++) {
        for (let numerator = 0; numerator <= denominator; numerator++) {
            const fraction = numerator / denominator;
            if (Math.abs(remainder - fraction) < tolerance) {
                if (whole === 0) {
                    return `${numerator}/${denominator}`;
                } else {
                    return `${whole} ${numerator}/${denominator}`;
                }
            }
        }
    }
    return result.toString();
}

// Display the calculator menu
function showMenu() {
    console.log("\n--- Calculator Menu ---");
    console.log("1. Addition (+)");
    console.log("2. Subtraction (-)");
    console.log("3. Multiplication (*)");
    console.log("4. Division (/)");
    console.log("5. Mixed Division (e.g., 2 1/2)");
    console.log("6. Exit");
    const choice = prompt("Choose an operation (1-6): ").trim();
    return choice;
}

// Main calculator function
function simpleCalculator() {
    console.log("Welcome to the Advanced Simple Calculator!");
    console.log("This calculator can perform addition, subtraction, multiplication, and division.");
    console.log("It supports both whole numbers, decimal numbers, and variable substitution.");

    // Load variables from cache
    let variables = loadCache();

    while (true) {
        const choice = showMenu();

        // Exit the calculator
        if (choice === '6') {
            console.log("Exiting the calculator. Goodbye!");
            saveCache(variables); // Save variables to cache before exiting
            break;
        }

        // Input the expression based on the chosen operation
        if (['1', '2', '3', '4', '5'].includes(choice)) {
            try {
                // Input the first number or variable
                let num1 = prompt("Enter the first number or variable: ").trim();
                if (variables.hasOwnProperty(num1)) {
                    num1 = variables[num1];
                } else {
                    num1 = parseFloat(num1);
                    if (isNaN(num1)) {
                        throw new Error("Invalid input! Please enter numeric values.");
                    }
                }

                // Input the second number or variable
                let num2 = prompt("Enter the second number or variable: ").trim();
                if (variables.hasOwnProperty(num2)) {
                    num2 = variables[num2];
                } else {
                    num2 = parseFloat(num2);
                    if (isNaN(num2)) {
                        throw new Error("Invalid input! Please enter numeric values.");
                    }
                }

                let result, operation, mixedResult;

                // Perform the chosen operation
                switch (choice) {
                    case '1':
                        result = num1 + num2;
                        operation = "+";
                        break;
                    case '2':
                        result = num1 - num2;
                        operation = "-";
                        break;
                    case '3':
                        result = num1 * num2;
                        operation = "*";
                        break;
                    case '4':
                        if (num2 === 0) {
                            console.log("Error: Division by zero is not allowed!");
                            continue;
                        }
                        result = num1 / num2;
                        operation = "/";
                        break;
                    case '5':
                        if (num2 === 0) {
                            console.log("Error: Division by zero is not allowed!");
                            continue;
                        }
                        result = num1 / num2;
                        operation = "/";
                        mixedResult = mixedDivision(result);
                        console.log(`Mixed division result: ${mixedResult}`);
                        break;
                    default:
                        console.log("Invalid choice! Please choose a valid option (1-6).");
                        continue;
                }

                // Display the result
                console.log(`The result of ${num1} ${operation} ${num2} is: ${result}`);

                // Log the activity
                logActivity({
                    type: "calculation",
                    operation: operation,
                    num1: num1,
                    num2: num2,
                    result: result,
                    mixed_result: mixedResult || null
                });
            } catch (error) {
                console.log(`Error: ${error.message}`);
            }
        } else {
            console.log("Invalid choice! Please choose a valid option (1-6).");
        }
    }
}

// Run the calculator
simpleCalculator();
