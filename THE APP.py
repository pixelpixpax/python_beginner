tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        try:
            task_num = int(input("Which task number is done? "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = tasks[task_num - 1] + " (done)"
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        task_num = int(input("Which task number to delete? "))
        if 1 <= task_num <= len(tasks):
            del tasks[task_num - 1]
        else:
            print("Invalid task number.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
