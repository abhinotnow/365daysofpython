#dictionary based student grade tracker

students = {}
print("1. Add student\n2. View all students\n3. Remove student\n4. Update grade\n5. Search student\n6. Exit\n")

def one():
    name = input("Enter student's name: ")
    grade = int(input(f"Enter grade of {name}"))
    students[name] = grade

def two():
    for student,grade in students.items():
        print(f"{student}: {grade}")

def three():
    delete = input("Enter student's name to be deleted: ")
    if delete in students.keys():
        del students[delete]
    else:
        print("Student does not exist.")

def four():
    student = input("Enter name of student: ")
    if student in students.keys():
        grade = int(input("Enter grade: "))
        students[student] = grade
    else:
        print("Student does not exist.")

def five():
    student = input("Search: ").lower()
    matches = [name for name in students if student in name.lower()]
    if matches:
        for m in matches:
            print(m, ":", students[m])
    else:
        print("No matching students found.")

def operation():
    while True:
        o = int(input("Enter an operation: "))
        if o == 1:
            one()
        elif o == 2:
            two()
        elif o == 3:
            three()
        elif o == 4:
            four()
        elif o == 5:
            five()
        elif o == 6:
            two()
            break

operation()
if students:
    print(f"Average grade of the class is: {sum(students.values())/len(students)}")
else: 
    print("No students in the class.")
