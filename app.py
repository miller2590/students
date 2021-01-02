student_list = []


def create_student():
    new_name = input("Name: ").capitalize()
    new_student = {'name': new_name,
                   'marks': []
                   }
    return new_student


def update_marks(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    if len(student['marks']) == 0:
        return 0

    total = sum(student['marks'])
    average = total / len(student['marks'])
    return average


def print_student_details(student):
    print(f"""{student['name']} 
    Grades: {student['marks']} 
    Average: {calculate_average_mark(student)}.""")


def print_student_list(students):
    for i, student in enumerate(students):
        print(f"ID: {i}")
        print_student_details(student)


def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark: "))
            update_marks(student, new_mark)

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


menu()
