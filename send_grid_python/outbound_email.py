"""This module uses simple SendGrid API to send email via a local FlaskApp."""
import logging
from environs import Env
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
sendgrid_env = Env()
sendgrid_env.read_env()


def send_email_message(
    subject: str,
    task: str,
    deadline: str,
    **kwargs,
) -> None:
    """
    This function sends a task reminder email
    Args:
        subject (str): The subject of the email reminder.
        task (str): The task information: example, update your bank account password.
        deadline (str): 2023-10-21.
        **kwargs: if wants to pass in custom to_emails or custom from_emails.
    """
    from_email = kwargs.get("from_email", sendgrid_env("from_email"))
    to_emails = kwargs.get("to_emails", sendgrid_env.list("to_emails"))

    email_message = Mail(
        from_email=from_email,
        to_emails=to_emails,
    )
    email_message.dynamic_template_data = {
        "subject": subject,
        "task": task,
        "deadline": deadline,
    }
    email_message.template_id = sendgrid_env("template_id")
    try:
        sendgrid_client = SendGridAPIClient(api_key=sendgrid_env("SENDGRID_API_KEY"))
        email_response = sendgrid_client.send(message=email_message)
        LOGGER.info(
            "Successfully sent the email with response status code: %s",
            email_response.status_code,
        )
    except Exception as exc:
        LOGGER.error("There was an error sending email via SendGrid API", exc_info=exc)
        raise exc
