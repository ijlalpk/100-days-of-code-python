def main():
    tasks = []

    while True:
        print("\nSmall App: Task Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("No task entered.")
        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
            else:
                print("No tasks yet.")
        elif choice == "3":
            if tasks:
                print("\nSelect a task number to remove:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                selection = input("Task number: ").strip()
                if selection.isdigit():
                    index = int(selection) - 1
                    if 0 <= index < len(tasks):
                        removed = tasks.pop(index)
                        print(f"Removed task: {removed}")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
