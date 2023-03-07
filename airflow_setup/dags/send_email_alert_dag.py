# pylint: disable=pointless-statement, wrong-import-position, import-error
"""This sets up email alert for tasks"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "configurations"))
from datetime import datetime, timedelta
from typing import Dict, Any

from airflow.decorators import dag
from airflow.operators.email import EmailOperator

from quarterly_reminder_configuration import (
    quarterly_subjects,
    quarterly_task_ids,
    quarterly_task_names,
    quarterly_deadlines,
)

from monthly_reminder_configuration import (
    monthly_subjects,
    monthly_task_ids,
    monthly_task_names,
    monthly_deadlines,
)

from yearly_reminder_configuration import (
    yearly_subjects,
    yearly_task_ids,
    yearly_task_names,
    yearly_deadlines,
)

default_args: Dict[str, Any] = {
    "owner": "mindy",
    "retry_delay": timedelta(minutes=1),
}

START_DATE: datetime = datetime(year=2022, month=12, day=29)


def create_html_content(task_name, deadline):
    """Create html content based upon task_name and deadline."""
    return f"""
    <p>Hello!</p>
    <p>This email is to remind you to complete the following task:</p>
    <p>Task Name: <b>{task_name}</b>.</p>
    <p>The deadline is <b>{deadline}</b>.</p>
    <p>Thanks!</p>
    """


@dag(
    dag_id="monthly_reminders",
    schedule="00 00 * * 6#1",
    start_date=START_DATE,
    catchup=False,
    default_args=default_args,
)
def monthly_reminders():
    """This function creates the monthly reminders dag."""
    for i, task_id in enumerate(monthly_task_ids):
        monthly_email_alert = EmailOperator(
            task_id=task_id,
            to=os.environ["email"],
            subject=monthly_subjects[i],
            html_content=create_html_content(
                task_name=monthly_task_names[i],
                deadline=monthly_deadlines[i],
            ),
        )

        monthly_email_alert


monthly_reminders()


@dag(
    dag_id="quarterly_reminders",
    schedule="00 00 1 */3 *",
    start_date=START_DATE,
    catchup=False,
    default_args=default_args,
)
def quarterly_reminders():
    """This function creates the quarterly reminders dag."""
    for i, task_id in enumerate(quarterly_task_ids):
        email_alert_quarterly = EmailOperator(
            task_id=task_id,
            to=os.environ["email"],
            subject=quarterly_subjects[i],
            html_content=create_html_content(
                task_name=quarterly_task_names[i],
                deadline=quarterly_deadlines[i],
            ),
        )
        email_alert_quarterly


quarterly_reminders()


@dag(
    dag_id="yearly_reminders",
    schedule="00 00 30 12 *",
    start_date=START_DATE,
    catchup=False,
    default_args=default_args,
)
def yearly_reminders():
    """This function creates the quarterly reminders dag."""
    for i, task_id in enumerate(yearly_task_ids):
        email_alert_quarterly = EmailOperator(
            task_id=task_id,
            to=os.environ["email"],
            subject=yearly_subjects[i],
            html_content=create_html_content(
                task_name=yearly_task_names[i],
                deadline=yearly_deadlines[i],
            ),
        )
        email_alert_quarterly


yearly_reminders()
