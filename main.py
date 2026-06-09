from task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    track_progress
)

tasks = []


def display_menu():
    print("\nTask Management System")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Task Name: ")
        description = input("Description: ")
        due_date = input("Due Date (YYYY-MM-DD): ")
        priority = input("Priority (1-5): ")

        if add_task(tasks, task_name, description, due_date, priority):
            print("Task added successfully!")
        else:
            print("Invalid task details.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}: {task['task_name']} ({status})")

        try:
            index = int(input("Enter task index to complete: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if mark_task_complete(tasks, index):
            print("Task marked as complete!")
        else:
            print("Invalid task index.")

    elif choice == "3":
        pending_tasks = view_pending_tasks(tasks)

        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("\nPending Tasks:")
            for task in pending_tasks:
                print(
                    f"- {task['task_name']} | "
                    f"Due: {task['due_date']} | "
                    f"Priority: {task['priority']}"
                )

    elif choice == "4":
        progress = track_progress(tasks)
        print(f"Progress: {progress}%")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")