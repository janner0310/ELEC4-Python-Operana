# Name: JOFIL OPERAÑA
# Section: IV-BSIT-B
# Activity: P2 - Python Modules
# Date: November 27, 2026

import calculator

def display_menu():
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("\nInvalid input! Please select 1 to 5.")
            continue

        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = calculator.add(num1, num2)

            elif choice == "2":
                result = calculator.subtract(num1, num2)

            elif choice == "3":
                result = calculator.multiply(num1, num2)

            elif choice == "4":
                result = calculator.divide(num1, num2)

            print("\nResult:", result)

        except ValueError:
            print("\nInvalid input! Please enter numeric values.")


main()
