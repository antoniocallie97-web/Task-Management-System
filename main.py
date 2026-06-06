from task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)


def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input()
            description = input()
            due_date = input()
            add_task(title, description, due_date)

        elif choice == "2":
            try:
                index = int(input())
                mark_task_as_complete(index)
            except ValueError:
                pass

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            print(calculate_progress())

        elif choice == "5":
            print("Exiting the program...")
            break


if __name__ == "__main__":
    main()