from datetime import datetime


def validate_task_name(task_name):
    return isinstance(task_name, str) and len(task_name.strip()) > 0


def validate_description(description):
    return isinstance(description, str) and len(description.strip()) > 0


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_priority(priority):
    try:
        priority = int(priority)
        return 1 <= priority <= 5
    except ValueError:
        return False