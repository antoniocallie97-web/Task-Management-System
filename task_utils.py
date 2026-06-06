from datetime import datetime

# Import validation functions
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title!")
        return

    if not validate_task_description(description):
        print("Invalid description!")
        return

    if not validate_due_date(due_date):
        print("Invalid due date! Use YYYY-MM-DD format.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task index!")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    for i, task in enumerate(pending):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
        return progress

    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100
    return progress