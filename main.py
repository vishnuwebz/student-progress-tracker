# Project: Student Progress Tracker

def main():
    print("==================================")
    print("Student Progress Tracker (CLI)")
    print("==================================")
    print("\n[Module 3] Collecting basic details and marks for one student...\n")

    # getting input from the user (*all inputs first come as strings)
    student_name = input("Enter student name: ")
    age_input = input("Enter student age: ")
    course = input("Enter course name: ")

    # type conversion (string -> int) with a simple assumption it is valid
    age = int(age_input)

    print("\nEnter marks for 3 subjects (0 to 100):")
    mark1 = float(input("Mark 1: "))
    mark2 = float(input("Mark 2: "))
    mark3 = float(input("Mark 3: "))


    # arithmetic operations
    total = mark1 + mark2 + mark3        # + addition
    average = total / 3                  # / normal division gives float
    average_floor = total // 3           # // floor division drops decimal part
    remainder = total % 3                # % remainder

    # --- Output summary ---
    print("\n--- Student Summary ---")
    print("Name   :", student_name)
    print("Age    :", age)
    print("Course :", course)
    print("Marks  :", mark1, mark2, mark3)
    print("Total  :", total)
    print("Average (float)      :", average)
    print("Average (floor // 3) :", average_floor)
    print("Remainder (total % 3):", remainder)


    print("\n[Info] In this module we used:")
    print("- Numeric types: int (age), float (marks).")
    print("- Arithmetic operations: +, /, //, % for calculations.")

if __name__ == "__main__":
    main()