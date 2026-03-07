# Module 6 - Sets and Dictionaries for Student Records
# Project: Student Progress Tracker

def main():
    print("===================================")
    print("   Student Progress Tracker (CLI)  ")
    print("===================================")
    print("\n[Module 6] Using sets and dictionaries for a student record...\n")

    # --- Basic details ---
    full_name = input("Enter full name (e.g., Vishnu G): ")
    age = int(input("Enter age: "))
    course = input("Enter course name: ")

    # --- Unique subjects using a set ---
    # We start from a list (could have duplicates) then convert to set to ensure uniqueness
    raw_subjects = ["Maths", "Science", "English", "Maths"]
    subject_set = set(raw_subjects)  # set removes duplicate "Maths"

    print("\nSubjects available (unique from set):")
    for subject in subject_set:
        print("-", subject)

    # For stable order when asking marks, convert back to a list
    subjects = list(subject_set)

    print("\nEnter marks for each subject (0 to 100):")
    marks = []
    for subject in subjects:
        mark = float(input(f"{subject} mark: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)

    # --- Dictionary for student record ---
    student = {
        "name": full_name,
        "age": age,
        "course": course,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "average": average,
    }

    # --- Output summary ---
    print("\n--- Student Dictionary Record ---")
    print("Raw dict :", student)
    print("\nAccess via keys:")
    print("Name     :", student["name"])
    print("Age      :", student["age"])
    print("Course   :", student["course"])
    print("Total    :", student["total"])
    print("Average  :", student["average"])

    print("\nSubjects and Marks from dict:")
    for i, subject in enumerate(student["subjects"]):
        print(f"- {subject}: {student['marks'][i]}")

    print("\n[Info] In this module we used:")
    print("- Set to ensure unique subjects (no duplicates).")
    print("- Dictionary to store a full student record with key-value pairs.")
    print("- Accessing and printing values via dictionary keys.")

if __name__ == "__main__":
    main()
