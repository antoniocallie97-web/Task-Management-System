from datetime import datetime


def validate_task_title(title):
    return isinstance(title, str) and title.strip() != ""


def validate_task_description(description):
    return isinstance(description, str)


def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False