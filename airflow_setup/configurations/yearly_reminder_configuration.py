"""This module contains all configuration information for yearly reminders."""
from typing import List

yearly_task_names: List[str] = [
    "review yearly goals",
    "schedule for doctor appointments",
    "schedule for dental appointments",
]

yearly_task_ids: List[str] = [
    task.replace(" ", "_") + "_email_alert_yearly" for task in yearly_task_names
]

yearly_subjects: List[str] = [task + " yearly reminder" for task in yearly_task_names]

yearly_deadlines: List[str] = [
    "in a week",
    "in two weeks",
    "in three weeks",
]
