# Module 9 - Functions and Lambda
# Project: Student Progress Tracker

def calculate_grade(average):
    """Return grade based on average marks."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def create_student():
    """Create and return a single student dictionary."""
    print("\n[Add Student]")
    full_name = input("Enter full name: ")
    age = int(input("Enter age: "))
    course = input("Enter course name: ")

    # Subjects: unique using set, then back to list
    raw_subjects = ["Maths", "Science", "English", "Maths"]
    subject_set = set(raw_subjects)
    subjects = list(subject_set)

    print("\nEnter marks for each subject (0 to 100):")
    marks = []
    for subject in subjects:
        mark = float(input(f"{subject} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)

    # Lambda to compute percentage w.r.t. maximum total (assuming 100 per subject)
    max_total = len(marks) * 100
    percentage = (lambda t, max_t: (t / max_t) * 100)(total, max_total)

    grade = calculate_grade(average)

    student = {
        "name": full_name,
        "age": age,
        "course": course,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": grade,
    }
    return student


def add_student(students):
    """Wrapper to create a student and add to the list."""
    student = create_student()
    students.append(student)
    print(f"\n[OK] Added student '{student['name']}' with grade {student['grade']} "
          f"({student['percentage']:.2f}% ).")


def list_students(students):
    """List all students with basic info."""
    print("\n[List Students]")
    if not students:
        print("No students have been added yet.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Total      :", student["total"])
        print("Average    :", student["average"])
        print("Percentage :", f"{student['percentage']:.2f}%")
        print("Grade      :", student["grade"])


def show_menu():
    """Print main menu options."""
    print("\n[Module 9] Main Menu")
    print("1. Add student")
    print("2. List students")
    print("3. Exit")


def main():
    print("===================================")
    print("   Student Progress Tracker (CLI)  ")
    print("===================================")

    students = []

    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[Warning] Invalid choice, please try again.")
            continue

        print("\n[Info] You can continue using the menu, or choose 3 to exit.")

if __name__ == "__main__":
    main()
