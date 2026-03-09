# menu.py

# Menu, main loop, and file save/load

from student_utils import add_student, list_students # import from custom module
from storage import save_students, load_students # new import

def show_menu():
    """Print main menu options."""
    print("\n[Module 11] Main Menu")
    print("1. Add student")
    print("2. List students")
    print("3. Save students to file")
    print("4. Exit")

def run_app():
    """Main loop for the Student Progress Tracker."""
    # load existing students from file (if any)
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
            # auto-save on exit as a convenience
            save_students(students)
            print("\nExiting program.Goodbye!")
            break
        else:
            print("\n[Warning] Invalid choice, please try again." )
            continue

        print("\n[Info] You can continue using the menu, or choose 3 to exit.")
