from datetime import datetime


def validate_task_title(title):
    """
    Title must be a non-empty string.
    """
    return isinstance(title, str) and title.strip() != ""


def validate_task_description(description):
    """
    Description must be a string (can be empty but not None).
    """
    return isinstance(description, str)


def validate_due_date(due_date):
    """
    Due date must be in format YYYY-MM-DD and be a valid date.
    """
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False