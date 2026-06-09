from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# Task list
tasks = []

# Task structure:
# {
#   "title": str,
#   "description": str,
#   "due_date": str,
#   "completed": bool
# }

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid task title!")
        return

    if not validate_task_description(description):
        print("Invalid task description!")
        return

    if not validate_due_date(due_date):
        print("Invalid due date!")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    real_index = index - 1

    if 0 <= real_index < len(tasks):
        tasks[real_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number!")


def view_pending_tasks(tasks=tasks):
    found = False

    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i+1}. {task['title']} - {task['description']} (Due: {task['due_date']})")
            found = True

    if not found:
        print("No pending tasks")


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    return (completed / len(tasks)) * 100