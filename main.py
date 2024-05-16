# list of dictionaries to store student info
students = [
    {"name": "Jake", "hometown": "New York", "favorite_food": "sushi"},
    {"name": "Callie", "hometown": "Boston", "favorite_food": "Tofu"},
    {"name": "Maddie", "hometown": "Plano", "favorite_food": "Pizza"}
]

# list names of students
def list_names(student_list):
    for index, student in enumerate(student_list, start=1):
        print(f"{index}. {student['name']}")

# get more info about a student
def get_student_info(index):
    return students[index]

#add new student
def add_student():
    new_student = {}
    new_student["name"] = input("Please input a name for the new student: ")
    new_student["hometown"] = input("Next please input their hometown: ")
    new_student["favorite_food"] = input("Last please input their favorite food: ")
    students.append(new_student)

# Main loop
while True:
    print("\nPlease select which action you'd like to do: add, view, or quit")
    action = input("> ").lower()

    if action == "add":
        add_student()
    elif action == "view":
        list_names(students)
        student_index = int(input("Which student would you like to learn more about? Enter a number 1-{}: ".format(len(students)))) - 1
        if 0 <= student_index < len(students):
            student_info = get_student_info(student_index)
            print(f"Student {student_index + 1} is {student_info['name']}. What would you like to know?")
            category = input("Enter 'hometown' or 'favorite food': ").lower()
            while category not in ['hometown', 'favorite food']:
                print("Invalid input. Please enter 'hometown' or 'favorite food'.")
                category = input("Enter 'hometown' or 'favorite food': ").lower()
            print(student_info['hometown' if category == 'hometown' else 'favorite_food'])
        else:
            print("Invalid student number. Please enter a number within the range.")
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'add', 'view', or 'quit'.")
