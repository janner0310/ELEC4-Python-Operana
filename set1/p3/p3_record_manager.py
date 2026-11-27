# Name: JOFIL OPERANA
# Section: IV-BSIT-B
# Activity: P3 - Lists and Sets
# Date: November 27, 2026


# List stores the original student names.
students = []

# Set stores normalized names to prevent duplicates.
student_lookup = set()


def add_student(students, student_lookup):
    name = input("Enter student name: ").strip()

    if not name:
        print("\nStudent name cannot be empty.")
        return

    normalized_name = " ".join(name.split()).casefold()

    if normalized_name in student_lookup:
        print("\nStudent already exists!")
    else:
        students.append(" ".join(name.split()))
        student_lookup.add(normalized_name)
        print(f"\n{name} successfully added!")


def remove_student(students, student_lookup):
    name = input("Enter student name to remove: ").strip()
    normalized_name = " ".join(name.split()).casefold()

    if not normalized_name:
        print("\nPlease enter a student name.")
        return

    for student in students:
        if " ".join(student.split()).casefold() == normalized_name:
            students.remove(student)
            student_lookup.remove(normalized_name)
            print(f"\n{student} has been removed.")
            return

    print("\nStudent not found.")


def search_students(students):
    keyword = input("Enter name to search: ").strip().casefold()

    if not keyword:
        print("\nPlease enter a search keyword.")
        return

    matches = [
        name for name in students
        if keyword in name.casefold()
    ]

    if matches:
        print("\nMatching students:")
        for name in matches:
            print("-", name)
    else:
        print("\nNo matching student found.")


def display_students(students):
    if not students:
        print("\nNo students in the record.")
        return

    sorted_students = sorted(students, key=str.casefold)

    print("\n===== STUDENT RECORDS =====")

    for index, name in enumerate(sorted_students, start=1):
        print(f"{index}. {name}")

    print(f"Total students: {len(students)}")


def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(students, student_lookup)

        elif choice == "2":
            remove_student(students, student_lookup)

        elif choice == "3":
            search_students(students)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("\nThank you for using Student Record Manager!")
            break

        else:
            print("\nInvalid input...Please select from 1 to 5.")


if __name__ == "__main__":
    main()


# Difference Between List and Set:
# A list stores items in order and allows duplicate entries, while a set only stores unique values.
# In this program, the students list is used to keep the student names for displaying and sorting.
# The student_lookup set is used to check if a student name already exists.
# Using both helps organize the student names and avoid duplicate entries.