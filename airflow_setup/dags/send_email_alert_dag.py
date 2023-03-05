# pylint: disable=pointless-statement
"""This sets up email alert for tasks"""
import os
from datetime import datetime, timedelta
from typing import Dict, Any

from airflow.decorators import dag
from airflow.operators.email import EmailOperator

default_args: Dict[str, Any] = {
    "owner": "mindy",
    "retry_delay": timedelta(minutes=1),
}

START_DATE: datetime = datetime(year=2023, month=1, day=1)


@dag(
    dag_id="monthly_reminder",
    schedule_interval="00 00 * * 6#1",
    start_date=START_DATE,
    catchup=False,
    default_args=default_args,
)
def monthly_reminder():
    """This function creates the monthly reminder dag."""
    monthly_email_alert = EmailOperator(
        task_id="email_alert_monthly",
        to=os.environ["email"],
        subject="task alert monthly",
        html_content="test task monthly.",
    )

    monthly_email_alert


monthly_reminder()


@dag(
    dag_id="quarterly_reminder",
    schedule_interval="00 00 1 */3 *",
    start_date=START_DATE,
    catchup=False,
    default_args=default_args,
)
def quarterly_reminder():
    """This function creates the quarterly reminder dag."""
    email_alert_quarterly = EmailOperator(
        task_id="email_alert_monthly",
        to=os.environ["email"],
        subject="task alert quarterly",
        html_content="test task quarterly.",
    )

    email_alert_quarterly


quarterly_reminder()
