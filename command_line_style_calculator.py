while True:
    user_input = input("Enter operation (or 'quit' to exit): ").strip()
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid format! Use: <operation> <num1> <num2>")
        continue
    operation = parts[0].lower()  
    try:
        num1 = float(parts[1])
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers! Please enter valid numbers.")
        continue
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            print("Error: Division by zero!")
            continue
        result = num1 / num2
    elif operation == "mod":
        result = num1 % num2
    elif operation == "pow":
        result = num1 ** num2
    else:
        print(f"Unknown operation '{operation}'! Use: add, sub, mul, div, mod, pow")
        continue
    print(f"Result: {result}")