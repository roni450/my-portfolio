tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    index = int(input("Enter task number to delete: "))
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\nMenu:\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
