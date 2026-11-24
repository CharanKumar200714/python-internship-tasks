def show_tasks():
    # Display all tasks
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    # Add a new task
    task = input("Enter new task: ")
    tasks.append(task)
    # Save to file
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added!")

def remove_task():
    # Remove a task
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number!")

# Main menu loop
while True:
    print("\n1. Add  2. View  3. Remove  4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Bye!")
        break
    else:
        print("Invalid choice!")
