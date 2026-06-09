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
    tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if not task["completed"]:
            print(task)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed_tasks = sum(
            1 for task in tasks if task["completed"]
        )
        progress = (completed_tasks / len(tasks)) * 100

    return progress