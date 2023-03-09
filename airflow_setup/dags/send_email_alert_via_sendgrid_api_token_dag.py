# pylint: disable=pointless-statement, wrong-import-position, import-error,
# pylint: disable=duplicate-code, cell-var-from-loop
"""This sets up email alert for tasks"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "configurations"))
from datetime import datetime, timedelta
from typing import Dict, Any

from airflow.decorators import dag, task
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from send_grid_configuration import (
    send_grid_task_schedule,
    send_grid_dag_ids,
    send_grid_subjects,
    send_grid_tasks,
    send_grid_deadlines,
)

default_args: Dict[str, Any] = {
    "owner": "mindy",
    "retry_delay": timedelta(minutes=1),
}

START_DATE: datetime = datetime(year=2022, month=12, day=29)

FROM_EMAIL = os.environ["from_email"]
TO_EMAILS = os.environ["to_emails"]
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
TEMPLATE_ID = os.environ["template_id"]

for index in range(len(send_grid_tasks)):

    @dag(
        dag_id=send_grid_dag_ids[index],
        schedule=send_grid_task_schedule[index],
        start_date=START_DATE,
        catchup=False,
        default_args=default_args,
    )
    def email_reminders():
        """This function creates the email reminders dag."""

        @task
        def send_email_message_task(
            subject: str,
            task_info: str,
            deadline: str,
        ):
            """This function is called by airflow @task"""
            email_message = Mail(
                from_email=FROM_EMAIL,
                to_emails=TO_EMAILS.split(","),
            )
            email_message.dynamic_template_data = {
                "subject": subject,
                "task": task_info,
                "deadline": deadline,
            }
            email_message.template_id = TEMPLATE_ID

            sendgrid_client = SendGridAPIClient(api_key=SENDGRID_API_KEY)
            email_response = sendgrid_client.send(message=email_message)
            return email_response.status_code

        send_email_message_task(
            subject=send_grid_subjects[index],
            task_info=send_grid_tasks[index],
            deadline=send_grid_deadlines[index],
        )

    email_reminders()
