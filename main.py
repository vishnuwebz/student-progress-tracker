# Project: Student Progress Tracker

def main():
    print("==================================")
    print("Student Progress Tracker (CLI)")
    print("==================================")
    print("\n[Module 4] Working with student names as strings...\n")

    # get basic details
    full_name = input("Enter full name (e.g., Vishnu G) : ")
    course = input("Enter course name (e.g, Python Full Stack) : ")

    # normalize course display
    course_clean = course.strip()

    # string indexing
    first_char = full_name[0] if len(full_name) > 0 else ""
    last_char = full_name[-1] if len(full_name) > 0 else ""

    # string slicing: first name and last name
    # we try to split on the first space
    space_index = full_name.find(" ")


    if space_index != -1:
        first_name = full_name[:space_index]        # from start to space-1
        last_name = full_name[space_index + 1:]     # from char after space to end

    else:
        first_name = full_name
        last_name = ""

    # some string transformation
    full_upper = full_name.upper()
    full_lower = full_name.lower()

    # --- Output summary ---
    print("\n--- String Details ---")
    print("Full Name          :", full_name)
    print("First character    :", first_char)
    print("Last character     :", last_char)
    print("First name (slice) :", first_name)
    print("Last name (slice)  :", last_name)
    print("Full upper case    :", full_upper)
    print("Full lower case    :", full_lower)
    print("Course (clean)     :", course_clean)


    print("\n[Info] In this module we used:")
    print("- String indexing: name[0], name[-1].")
    print("- String slicing: name[:space_index], name[space_index+1:].")
    print("- String methods: .upper(), .lower(), .strip().")

if __name__ == "__main__":
    main()