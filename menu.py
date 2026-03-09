# menu.py

# Menu and main loop

from student_utils import add_student, list_students # import from custom module

def show_menu():
    """Print main menu options."""
    print("\n[Module 10] Main Menu")
    print("1. Add student")
    print("2. List students")
    print("3. Exit")

def run_app():
    """Main loop for the Student Progress Tracker."""
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
            print("\n[Warning] Invalid choice, please try again." )
            continue

        print("\n[Info] You can continue using the menu, or choose 3 to exit.")
