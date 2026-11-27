# Name: JOFIL OPERANA
# Section: IV-BSIT-B
# Activity: P4 - Exception Handling
# Date: November 27, 2026

def display_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide Two Numbers")
    print("2. Open and Read a File")
    print("3. Exit")

def divide_numbers():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("\nInvalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("\nCannot divide by zero.")

    else:
        print(f"\nResult: {result}")

    finally:
        print("Division operation completed.")