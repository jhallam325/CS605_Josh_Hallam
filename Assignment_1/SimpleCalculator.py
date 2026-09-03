# Source - https://stackoverflow.com/a/518007
# Posted by Ryan Duffield, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-01, License - CC BY-SA 4.0

import os
clear = lambda: os.system('cls')
clear()

# My code:

print("Welcome, to the Simple Calculator of Yesterday!")

run_calculator = True

while run_calculator:
    input1 = input("\nEnter your first  number: ")
    input2 = input("Enter your second number: ")

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation_values = ["1", "2", "3", "4"]
    operation = input("\nSelect an operation: ")

    while operation not in operation_values:
        print("\nYou must choose a whole number 1-4.")
        operation = input("Select an operation: ")

    result = 0;
    number1 = float(input1)
    number2 = float(input2)
    print()

    if operation == "1":
        result = number1 + number2
        print(f"Result: {number1} + {number2} = {result}")
    elif operation == "2":
        result = number1 - number2
        print(f"Result: {number1} - {number2} = {result}")
    elif operation == "3":
        result = number1 * number2
        print(f"Result: {number1} * {number2} = {result}")
    else:
        result = number1 / number2
        print(f"Result: {number1} / {number2} = {result}")


    another_calculation = input("\nWould you like to perform another calculation? (yes/no): ")
    another_calculation = another_calculation.upper()

    while another_calculation[0] != 'Y' and another_calculation[0] != 'N':
        print("\nYou need to choose yes or no.")
        another_calculation = input("Would you like to perform another calculation? (yes/no): ")
        another_calculation = another_calculation.upper()
    
    if another_calculation[0] == 'Y':
        run_calculator = True
        print()
    else:
        run_calculator = False
        print("\nThanks for using my calculator! Goodbye!")

