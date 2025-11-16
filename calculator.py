def run_calculator():
    print("Welcome to the Python Calculator!")
    print("Enter a mathematical expression (e.g., 10 + 5 * 2)")
    print("Type 'q' or 'quit' to exit.")

    while True:
        # 1. Get input from the user
        user_input = input(">>> ")

        # 2. Check if the user wants to quit
        if user_input.lower() in ['q', 'quit']:
            print("Goodbye!")
            break

        # 3. Try to calculate the result
        try:
            result = eval(user_input)
            print(f"Result: {result}")

        # 4. Handle errors (like invalid syntax or dividing by zero)
        except Exception as e:
            print(f"Error: Invalid expression. Please try again. ({e})")

if __name__ == "__main__":
    run_calculator()