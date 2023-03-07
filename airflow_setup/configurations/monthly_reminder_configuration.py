"""This module contains all configuration information for monthly reminders."""
from typing import List

monthly_task_names: List[str] = [
    "review monthly expenses",
    "monthly reflection journal",
    "monthly fitness check-ins",
    "monthly new book choice",
]

monthly_task_ids: List[str] = [
    task.replace(" ", "_") + "_email_alert_quarterly" for task in monthly_task_names
]

monthly_subjects: List[str] = [
    task + " quarterly reminder" for task in monthly_task_names
]

monthly_deadlines: List[str] = [
    "in a day",
    "in two days",
    "in a day",
    "in a day",
]
