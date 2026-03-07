def main():
    print("==================================")
    print("Student Progress Tracker (CLI)")
    print("==================================")
    print("\n[Module 2] Collecting basic student details...\n")

    # getting input from the user (*all inputs first come as strings)
    student_name = input("Enter student name: ")
    age_input = input("Enter student age: ")
    course = input("Enter course name: ")

    # type conversion (string -> int) with a simple assumption it is valid
    age = int(age_input)

    years_to_25 = 25 - age

    print("\n--- Student Summary ---")
    print("Name :", student_name)
    print("Age :", age)
    print("Course :", course)
    print(f"{student_name} will be 25 in {years_to_25} year(s)")


if __name__ == "__main__":
    main()