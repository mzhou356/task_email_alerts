"""This module contains all configuration information for quarterly reminders."""
from typing import List


quarterly_task_names: List[str] = [
    "review quarterly goals",
    "reallocate portfolio",
    "readjust workout plans",
    "plan quarterly vacation",
]

quarterly_task_ids: List[str] = [
    task.replace(" ", "_") + "_email_alert_quarterly" for task in quarterly_task_names
]

quarterly_subjects: List[str] = [
    task + " quarterly reminder" for task in quarterly_task_names
]

quarterly_deadlines: List[str] = [
    "in a week",
    "in two weeks",
    "in a week",
    "in three weeks",
]
