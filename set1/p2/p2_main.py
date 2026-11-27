# Name: JOFIL OPERANA
# Section: IV-BSIT-B
# Activity: P2 - Custom Module
# Date: November 27, 2026

import student_utils
from datetime import datetime


def main():
    grades = []

    print("===== STUDENT GRADE REPORT =====")

    while True:
        try:
            number = int(input("How many grades do you want to enter? "))

            if number > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade No.{i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    print("\n===== GRADE RESULTS =====")
    print("Grades:", grades)
    print("Average:", student_utils.calculate_average(grades))
    print("Highest:", student_utils.get_highest(grades))
    print("Lowest:", student_utils.get_lowest(grades))

    print("Status:", student_utils.check_pass_fail(grades))

    print("\nReport generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))


if __name__ == "__main__":
    main()
