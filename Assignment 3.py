# Build a student grade management system using the following Python concepts:
# - List of dictionaries
# - Function with required arguments, *args, **kwargs
# - Function decorator
# - Loops and control statements

# Requirements
# 1. Use a *decorator* to log function activity.
# 2. Use a function to *add student data* using *args and **kwargs.
# 3. Store student records in a *list of dictionaries*.
# 4. Use *loops and conditionals* to calculate and display results.

# Decorator to show when a function starts and ends
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Start: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"End: {func.__name__}\n")
        return result
    return wrapper

# List to store student details
students = []

# Function to add a student
@log
def add_student(name, *marks, **info):
    student = {
        'name': name,
        'marks': marks,
        'info': info
    }
    students.append(student)

# Function to show results
@log
def show_results():
    for s in students:
        print(f"Student: {s['name']}")
        avg = sum(s['marks']) / len(s['marks'])

        if avg >= 90:
            grade = 'A'
        elif avg >= 75:
            grade = 'B'
        elif avg >= 60:
            grade = 'C'
        else:
            grade = 'D'

        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")
        if s['info']:
            print("Extra Info:", s['info'])
        print("-" * 30)

# Adding students
add_student("Pooji", 85, 90, 98, age=21, branch="EEE")
add_student("Lucky", 90, 88, 85)
add_student("Raj", 85, 90, 88, branch="EEE")

# results
show_results()