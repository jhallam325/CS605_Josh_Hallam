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
    # Source - https://stackoverflow.com/a/16290419
    # Posted by abarnert, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-09-03, License - CC BY-SA 3.0
    while True:
        try:
            number1 = float(input ("\nEnter your first number: "))
        except ValueError:
            print("Enter a number!")
        else:
            break

    while True:
        try:
            number2 = float(input ("Enter your second number: "))
        except ValueError:
            print("Enter a number!")
        else:
            break
    
    # My code:
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
        number2_is_zero = (number2 == 0)
        while number2_is_zero:
            first_time_zero = True
            while True:
                try:
                    if first_time_zero:
                        print("Your number can't be zero, otherwise you'll divide by 0!")
                    number2 = float(input ("Enter your second number: "))
                    first_time_zero = False
                except ValueError:
                    print("Enter a number!")
                else:
                    if (number2 != 0):
                        number2_is_zero = (number2 == 0)
                        break
                    else:
                        print("Your number can't be zero, otherwise you'll divide by 0!")

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

