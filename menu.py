# menu.py
#Menu, main loop

from student_utils import add_student, list_students
from storage import save_students, load_students


def show_menu():
    """Print main menu options."""
    print("\n===== Student Progress Tracker Menu =====")
    print("1. Add student")
    print("2. List students")
    print("3. Save students to file")
    print("4. Exit")


def run_app():
    """Main loop for the Student Progress Tracker."""
    print("\n[Info] Loading existing students (if any)...")
    students = load_students()

    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            save_students(students)
        elif choice == "4":
            save_students(students)  # auto-save on exit
            print("\nThank you for using Student Progress Tracker. Goodbye!")
            break
        else:
            print("\n[Warning] Invalid choice, please try again.")
            continue

        print("\n[Info] You can continue using the menu, or choose 4 to exit.")
