# Project: Student Progress Tracker

def main():
    print("==================================")
    print("Student Progress Tracker (CLI)")
    print("==================================")
    print("\n[Module 5] Using lists and tuples for subjects and marks...\n")

    # get basic details
    full_name = input("Enter full name (e.g., Vishnu G) : ")
    age = int(input("Enter age: "))
    course = input("Enter course name (e.g, Python Full Stack) : ")

    # pack some basic info in a tuple(immutable container)
    student_basic = (full_name, age, course)

    # --- students and marks using a list ---
    # predefined subjects lists (can be changed later)
    subjects = ["Maths", "Physics", "Chemistry"]
    marks = [] # empty list to store marks

    print("\nEnter marks for each subject (0 to 100):")
    for subject in subjects:
        mark = float(input(f"{subject} mark: "))
        marks.append(mark) # list.append() to add elements at end

    # calculate total and average using the marks list
    total = sum(marks)
    average = total / len(marks)

    # --- output summary ---
    print("\n--- Student Summary (lists and tuples)---")
    print("Student (tuple) :", student_basic)
    print("Name            :", student_basic[0])
    print("Age             :", student_basic[1])
    print("Course          :", student_basic[2])

    print("\nSubjects and Marks:")
    for index, subject in enumerate(subjects):
        print(f"{index}. {subject}: {marks[index]}")

    print("\nTotal marks :", total)
    print("Average : ", average)


    print("\n[Info] In this module we used:")
    print("- List for multiple marks and subjects.")
    print("- .append() to add marks to the list.")
    print("- Tuple to store basic, fixed student info.")
    print("- Indexing and enumerate() to access list items.")

if __name__ == "__main__":
    main()