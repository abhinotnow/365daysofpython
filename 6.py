tasks = []
print(" 1. Add a task \n 2. View all tasks \n 3. Remove a task \n 4. Insert a task at a position \n 5. Search tasks \n 6. Exit")

def operation():
    o = int(input("Enter an operation: "))
    if(o == 1):
        one()
        operation()
    elif(o == 2):
        two()
        operation()
    elif(o == 3):
        three()
        operation()
    elif(o == 4):
        four()
        operation()
    elif (o==5):
        five()
        operation()
    elif(o == 6):
        two()

def two():
    for i in range(len(tasks)):
        print(f"{i+1}. " + tasks[i])

def one():
    tasks.append(input("Enter the task: "))

def three():
    two()
    remove = int(input("Choose a task to remove: "))
    if 1<= remove <= len(tasks):
        tasks.pop(remove-1)
    else:
        print("Given task does not exist.")

def four():
    two()
    task = input("Enter task to be inserted: ")
    insert = int(input("Enter position of task: "))
    tasks.insert(insert, task)

def five():
    count = 0 
    keyword = input("Enter the search keyword: ")
    for i in range(len(tasks)):
        if keyword in tasks[i]:
            print(f"{i+1}. "+tasks[i])
        else:
            count +=1
    if count == len(tasks):
        print("No such task exists yet.")
operation()
    
