from validation import (
    validate_task_name,
    validate_description,
    validate_due_date,
    validate_priority
)


def add_task(tasks, task_name, description, due_date, priority):
    if not validate_task_name(task_name):
        return False

    if not validate_description(description):
        return False

    if not validate_due_date(due_date):
        return False

    if not validate_priority(priority):
        return False

    task = {
        "task_name": task_name,
        "description": description,
        "due_date": due_date,
        "priority": int(priority),
        "completed": False
    }

    tasks.append(task)
    return True


def mark_task_complete(tasks, task_index):
    try:
        task_index = int(task_index)
    except ValueError:
        return False

    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        return True

    return False


def view_pending_tasks(tasks):
    return [task for task in tasks if not task["completed"]]


def track_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    return int((completed / len(tasks)) * 100)