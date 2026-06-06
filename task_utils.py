from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title!")
        return

    if not validate_task_description(description):
        print("Invalid description!")
        return

    if not validate_due_date(due_date):
        print("Invalid due date!")
        return

    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })

    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index!")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    pending = [t for t in tasks if not t["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100