# student_utils.py
# Student-related functions using Student class

from models import Student


def safe_int_input(prompt: str) -> int:
    """Ask for an integer until the user gives a valid one."""
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("[Error] Please enter a valid integer.")


def safe_float_input(prompt: str) -> float:
    """Ask for a float until the user gives a valid one."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("[Error] Please enter a valid number (e.g., 75 or 89.5).")

def create_student():
    """Create and return a single student dictionary."""
    print("\n[Add Student]")
    full_name = input("Enter full name: ")
    age = safe_int_input("Enter age: ")
    course = input("Enter course name: ")

    # Subjects: unique using set, then back to list
    raw_subjects = ["Maths", "Science", "English", "Maths"]
    subject_set = set(raw_subjects)
    subjects = list(subject_set)

    print("\nEnter marks for each subject (0 to 100):")
    marks = []
    for subject in subjects:
        mark = safe_float_input(f"{subject} mark: ")
        marks.append(mark)

    # Create Student object
    student_obj = Student(
        name=full_name,
        age=age,
        course=course,
        subjects=subjects,
        marks=marks,
    )

    # Convert object to dict for compatibility with storage/UI
    student_dict = student_obj.to_dict()
    return student_dict


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
