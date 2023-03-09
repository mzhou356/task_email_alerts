"""This module contains send grid configuration."""
from typing import List

send_grid_task_schedule: List[str] = [
    "00 00 25 5 *",
    "00 00 25 7 *",
    "00 00 25 9 *",
]

send_grid_dag_ids: List[str] = [
    "couple_reminder_one",
    "couple_reminder_two",
    "couple_reminder_three",
]

send_grid_subjects: List[str] = [
    "happy anniversary",
    "happy birthday",
    "happy birthday",
]

send_grid_tasks: List[str] = [
    "buy gifts",
    "buy gift",
    "buy gift",
]

send_grid_deadlines: List[str] = [
    "in a few days",
    "in a few days",
    "in a few days",
]
