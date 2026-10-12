tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    if tasks:
        number = int(input("Enter task number to remove: "))
        if number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Removed:", removed)
        else:
            print("Invalid task number.")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")