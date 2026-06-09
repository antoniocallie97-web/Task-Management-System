from datetime import datetime

def validate_task_title(title):
    # Title must be a non-empty string
    return isinstance(title, str) and len(title.strip()) > 0


def validate_task_description(description):
    # Description must be a non-empty string
    return isinstance(description, str) and len(description.strip()) > 0


def validate_due_date(due_date):
    # Must match YYYY-MM-DD format
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False