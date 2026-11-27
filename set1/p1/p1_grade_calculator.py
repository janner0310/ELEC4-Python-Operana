
# Name: JOFIL OPERANA
# Section: IV-BSIT-B
# Activity: P1 - Functions
# Date: November 26, 2026



def get_grades():
    grades = []

    # Validate the number of grades
    while True:
        try:
            number = int(input("How many grades do you want to enter? "))

            if number > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Accept and validate individual grades
    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def check_pass_fail(grades):
    for grade in grades:
        if grade >= 75:
            print(f"{grade} - Passed")
        else:
            print(f"{grade} - Failed")


def display_menu():
    print("\n================================")
    print("       GRADE CALCULATOR")
    print("================================")
    print("1. Enter Grades")
    print("2. View Grade Results")
    print("3. Exit")
    print("================================")


def view_results(grades):
    while True:
        print("\n--- Grade Results ---")
        print("Grades:", grades)
        print("Average:", calculate_average(grades))
        print("Highest:", get_highest(grades))
        print("Lowest:", get_lowest(grades))

        print("\n--- Pass or Fail ---")
        check_pass_fail(grades)

        print("\n1. Back to Main Menu")
        print("2. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            return

        elif choice == "2":
            print("Thank you for using Grade Calculator!")
            return "exit"

        else:
            print("Invalid choice! Please select 1 or 2.")



def main():
    student_grades = []

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            student_grades = get_grades()
            print("Grades successfully saved!")

        elif choice == "2":
            if len(student_grades) == 0:
                print("Please enter grades first.")
            else:
                result = view_results(student_grades)

                if result == "exit":
                    break

        elif choice == "3":
            print("Thank you for using Grade Calculator!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()
