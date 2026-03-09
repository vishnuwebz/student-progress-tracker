# storage.py
# file handling for student progress tracker

import os

DATA_FILE = "students_data.txt"

def student_to_line(student: dict) -> str:
    """
    Convert a student dict to a single line string.
    Format:
    name|age|course|subject1,subject2|mark1,mark2|total|average|percentage|grade

    """
    subjects_str = ",".join(student["subjects"])
    marks_str = ",".join(str(m) for m in student["marks"])

    line = (
        f"{student['name']}|"
        f"{student['age']}|"
        f"{student['course']}|"
        f"{subjects_str}|"
        f"{marks_str}|"
        f"{student['total']}|"
        f"{student['average']}|"
        f"{student['percentage']}|"
        f"{student['grade']}"
    )
    return line

def line_to_student(line: str) -> dict:
    """Convert one line from file back to a student dict."""
    line = line.strip()
    if not line:
        return None

    parts = line.strip("|")
    if len(parts) != 9:
        return None # malformed line

    name, age_str, course, subjects_str, marks_str, total_str, avg_str, perc_str, grade = parts

    subjects = subjects_str.split(",") if subjects_str else []
    marks = [float(m) for m in marks_str.split(",")] if marks_str else []

    student = {
        "name": name,
        "age": int(age_str),
        "course": course,
        "subjects": subjects,
        "marks": marks,
        "total": float(total_str),
        "average": float(avg_str),
        "percentage": float(perc_str),
        "grade": grade,
    }
    return student

def save_students(students: list):
    """Save all students to a text file (overwrite)."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for student in students:
            line = student_to_line(student)
            f.write(line + "\n")
    print(f"\n[File] Saved {len(students)} student(s) to '{DATA_FILE}'.")

def load_students() -> list:
    """Load students from file, if it exists; otherwise return empty list."""
    if not os.path.exists(DATA_FILE):
        print(f"\n[File] '{DATA_FILE}' not found, starting with empty student list.'")
        return []
    students = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for line in f:
            student = line_to_student(line)
            if student:
                students.append(student)

    print(f"\n[File] Loaded {len(students)} students(s) from '{DATA_FILE}'.")
    return students