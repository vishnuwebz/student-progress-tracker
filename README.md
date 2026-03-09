# Student Progress Tracker (CLI)

A simple **Python command-line application** to manage student progress, built step by step as a fundamentals project.  
It tracks students, their subjects and marks, computes averages and grades, and persists data to a text file so it can be loaded later.  

This project was designed as a learning path to cover core Python topics (data types, control flow, functions, files, exceptions, and OOP with inheritance)

---

## Features

- Add **Normal** or **Graduate** students from the terminal  
- Store subjects and marks per student  
- Automatically compute **total**, **average**, **percentage**, and **grade**  
- Distinguish between Student and GraduateStudent (with thesis title) using **inheritance**  
- Menu-driven CLI with input validation and friendly error messages  
- Save and load all students to/from a text file (`students_data.txt`)  

---

## Concepts Covered

This project intentionally uses many Python fundamentals:

- Variables, input, type conversion (`int`, `float`, `str`)
- Numeric types and arithmetic operators
- Strings, indexing, slicing, and basic methods
- Lists, tuples, sets, and dictionaries
- `if / elif / else` conditional logic for grading
- `while True` loops, `for` loops, `break` and `continue`
- Functions, arguments, return values, and a simple `lambda`
- Modules and imports (`main.py`, `menu.py`, `student_utils.py`, `storage.py`, `models.py`)
- File handling with `open()`, read/write, and the `with` context manager
- Basic exception handling with `try/except` for user input and file I/O
- Object-Oriented Programming:
  - `Student` class with `__init__` constructor
  - Methods for total, average, percentage, and grade
  - `GraduateStudent` subclass with inheritance and method overriding

---

## Project Structure

```text
StudentProgressTracker/
├── main.py           # Entry point for the CLI app
├── menu.py           # Menu and main loop
├── student_utils.py  # Input helpers and student creation/listing
├── storage.py        # Save/load students to/from a text file
├── models.py         # Student and GraduateStudent classes
└── README.md         # This documentation


How to Run
Clone the repository:

bash
git clone https://github.com/vishnuwebz/student-progress-tracker.git
cd student-progress-tracker
Run the app:

bash
python main.py
Use the menu:

1 – Add student (choose Normal or Graduate, enter marks)

2 – List all students with summary

3 – Save students to students_data.txt

4 – Exit (auto-saves before quitting)

Python 3.8+ recommended.