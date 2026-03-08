# Module 6 - Sets and Dictionaries for Student Records
# Project: Student Progress Tracker
from os import name


def add_student(students):
    """Add one student with subjects, marks, average, grade."""
    print("\n[Add student]")
    full_name = input("Enter full name: ")
    age = int(input("Enter age: "))
    course = input("Enter course name: ")

    # subjects using a set to avoid duplicates
    raw_subjects = ["Maths", "Science", "Engineering", "Maths"]
    subject_set = set(raw_subjects)
    subjects = list(subject_set) # convert back to list for stable ordering

    print("\nEnter marks for each subject (0 to 100")
    marks = []
    for subject in subjects:
        mark = float(input(f"{subject} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = round(total / len(marks), 2)

    # grading logic (same scale as Module 7)
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name" : full_name,
        "age" : age,
        "course" : course,
        "marks" : marks,
        "total" : total,
        "average" : average,
        "grade" : grade,
    }

    students.append(student) # add this student to the list
    print(f"\n[OK] Added student '{full_name}' with grade {grade}.")

def list_students(students):
    """List all students with basic info."""
    print("\n[List Students]")
    if not students:
        print("No students have been added yet.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print("Name    :", student["name"])
        print("Age     :", student["age"])
        print("Course  :", student["course"])
        print("Total   :", student["total"])
        print("Average :", student["average"])
        print("Grade   :", student["grade"])

def main():
    print("===================================")
    print("   Student Progress Tracker (CLI)  ")
    print("===================================")

    students = []   # list of student dictionaries

    # main menu loop
    while True:
        print("\n[Module 8] Main Menu")
        print("1: Add student")
        print("2: List students")
        print("3: Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break   # break exists the while True loop
        else:
            print("\n[Warning] Invalid choice, please try again.")
            # continue will skip the rest of the loop body and go to the next iteration
            continue
        print("\n[Info] You can continue using the menu, or choose 3 to exit.")

if __name__ == "__main__":
    main()
