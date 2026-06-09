from task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    track_progress
)

tasks = []

while True:
    try:
        choice = input()

        if choice == "1":
            task_name = input()
            description = input()
            due_date = input()
            priority = input()

            if add_task(tasks, task_name, description, due_date, priority):
                print("Task added successfully!")

        elif choice == "2":
            index = input()
            if mark_task_complete(tasks, index):
                print("Task marked as complete!")

        elif choice == "3":
            pending = view_pending_tasks(tasks)
            for t in pending:
                print(f"{t['task_name']} {t['due_date']} {t['priority']}")

        elif choice == "4":
            print(f"{track_progress(tasks)}")

        elif choice == "5":
            break

    except EOFError:
        break