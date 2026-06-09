from datetime import datetime

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
    # assuming user input is 1-based index
    real_index = index - 1

    if 0 <= real_index < len(tasks):
        tasks[real_index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    has_pending = False

    for i, task in enumerate(tasks):
        if not task["completed"]:
            has_pending = True
            print(f"{i+1}. {task['title']} - {task['description']} (Due: {task['due_date']})")

    if not has_pending:
        print("No pending tasks")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100
    return progress