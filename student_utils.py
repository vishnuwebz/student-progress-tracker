# student_utils.py
# Student-related functions using inheritance

from models import Student, GraduateStudent


def safe_int_input(prompt: str) -> int:
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("[Error] Please enter a valid integer.")


def safe_float_input(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("[Error] Please enter a valid number (e.g., 75 or 89.5).")


def choose_student_type() -> str:
    """Let the user choose Normal vs Graduate student."""
    while True:
        print("\nChoose student type:")
        print("1. Normal Student")
        print("2. Graduate Student")
        choice = input("Enter choice (1/2): ").strip()
        if choice == "1":
            return "normal"
        elif choice == "2":
            return "graduate"
        else:
            print("[Warning] Invalid choice. Please enter 1 or 2.")


def create_student():
    """Create and return a student dict, based on Student or GraduateStudent."""
    print("\n[Add Student]")
    student_type = choose_student_type()

    full_name = input("Enter full name: ")
    age = safe_int_input("Enter age: ")
    course = input("Enter course name: ")

    thesis_title = ""
    if student_type == "graduate":
        thesis_title = input("Enter thesis title: ")

    # Subjects: unique using set, then back to list
    raw_subjects = ["Maths", "Science", "English", "Maths"]
    subject_set = set(raw_subjects)
    subjects = list(subject_set)

    print("\nEnter marks for each subject (0 to 100):")
    marks = []
    for subject in subjects:
        mark = safe_float_input(f"{subject} mark: ")
        marks.append(mark)

    # Create appropriate object based on type
    if student_type == "graduate":
        student_obj = GraduateStudent(
            name=full_name,
            age=age,
            course=course,
            subjects=subjects,
            marks=marks,
            thesis_title=thesis_title,
        )
    else:
        student_obj = Student(
            name=full_name,
            age=age,
            course=course,
            subjects=subjects,
            marks=marks,
        )

    student_dict = student_obj.to_dict()
    return student_dict


def add_student(students):
    """Wrapper to create a student and add to the list."""
    student = create_student()
    students.append(student)
    print(
        f"\n[OK] Added {student['type']} '{student['name']}' with grade {student['grade']} "
        f"({student['percentage']:.2f}% )."
    )
    if student.get("type") == "Graduate" and student.get("extra"):
        print(f"Thesis title: {student['extra']}")


def list_students(students):
    """List all students with basic info."""
    print("\n[List Students]")
    if not students:
        print("No students have been added yet.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print("Type       :", student.get("type", "Student"))
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("Total      :", student["total"])
        print("Average    :", student["average"])
        print("Percentage :", f"{student['percentage']:.2f}%")
        print("Grade      :", student["grade"])
        if student.get("type") == "Graduate" and student.get("extra"):
            print("Thesis     :", student["extra"])
