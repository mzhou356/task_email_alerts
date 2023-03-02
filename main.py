# pylint: disable=no-value-for-parameter
"""This is the main program for sending email alerts."""
from typing import Optional, Any, Dict

import click
from send_grid_python.outbound_email import send_email_message


@click.command()
@click.option(
    "--subject",
    default="task reminder email",
    type=str,
    required=False,
    help="enter the subject line for the email",
)
@click.option(
    "--task",
    type=str,
    required=True,
    help="enter the task to be reminded of.",
)
@click.option(
    "--deadline", type=str, required=True, help="enter the deadline for the task."
)
@click.option(
    "--from_email", default=None, type=str, required=False, help="enter the from email."
)
@click.option(
    "--to_emails",
    default=None,
    type=str,
    required=False,
    help="enter the list of to_emails without brackets and include comma.",
)
def run_send_email_via_sendgrid(
    subject: str,
    task: str,
    deadline: str,
    from_email: Optional[str],
    to_emails: Optional[str],
):
    """This is the main function."""
    command_inputs: Dict[str, Any] = {
        "subject": subject,
        "task": task,
        "deadline": deadline,
    }

    if from_email:
        command_inputs["from_email"] = from_email
    if to_emails:
        command_inputs["to_emails"] = to_emails.split(",")

    send_email_message(**command_inputs)


if __name__ == "__main__":
    run_send_email_via_sendgrid()
