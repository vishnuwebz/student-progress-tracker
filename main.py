# Module 6 - Sets and Dictionaries for Student Records
# Project: Student Progress Tracker

def main():
    print("===================================")
    print("   Student Progress Tracker (CLI)  ")
    print("===================================")
    print("\n[Module 7] Adding grading logic using if / elif / else...\n")

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

    # --- Grading logic using if / elif / else ---
    # Example scale (you can tweak later):
    # 90+  -> A
    # 75-89 -> B
    # 60-74 -> C
    # 40-59 -> D
    # <40   -> F
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

    # --- Dictionary for student record ---
    student = {
        "name": full_name,
        "age": age,
        "course": course,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "average": average,
        "grade" : grade,
    }

    # --- Output summary ---
    print("\n--- Student Record with Grade ---")
    print("Name    :", student["name"])
    print("Age     :", student["age"])
    print("Course  :", student["course"])
    print("Total   :", student["total"])
    print("Average :", student["average"])
    print("Grade   :", student["grade"])

    print("\nSubjects and Marks from dict:")
    for i, subject in enumerate(student["subjects"]):
        print(f"- {subject}: {student['marks'][i]}")

    print("\n[Info] In this module we used:")
    print("- if / elif / else to convert average marks into grade.")
    print("- Stored the grade inside the student dictionary as 'grade'.")

if __name__ == "__main__":
    main()
