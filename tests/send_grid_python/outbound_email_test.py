"""This python module tests outbound_email module."""
import pytest

from send_grid_python.outbound_email import send_email_message


def test_send_email_message__without_kwargs_succeeds(mocker, monkeypatch) -> None:
    """Test send_email_message without kwargs succeeds."""
    monkeypatch.setenv("to_emails", "test_to_emails")
    monkeypatch.setenv("from_email", "test_from_email")
    monkeypatch.setenv("SENDGRID_API_KEY", "test_key")
    monkeypatch.setenv("template_id", "test_template_id")
    subject = "test_subject"
    task = "test_task"
    deadline = "test_deadline"
    return_client_mock = mocker.Mock()
    api_client_mock = mocker.patch(
        "send_grid_python.outbound_email.SendGridAPIClient",
        return_value=return_client_mock,
    )
    message_mock = mocker.Mock()
    mail_mock = mocker.patch(
        "send_grid_python.outbound_email.Mail",
        return_value=message_mock,
    )

    send_email_message(
        subject=subject,
        task=task,
        deadline=deadline,
    )

    mail_mock.assert_called_once_with(
        from_email="test_from_email", to_emails=["test_to_emails"]
    )
    assert message_mock.template_id == "test_template_id"
    assert message_mock.dynamic_template_data == {
        "subject": subject,
        "task": task,
        "deadline": deadline,
    }
    api_client_mock.assert_called_once_with(api_key="test_key")
    return_client_mock.send.assert_called_once_with(message=message_mock)


def test_send_email_message_with_kwargs_succeeds(mocker, monkeypatch) -> None:
    """Test send_email_message with kwargs succeeds."""
    monkeypatch.setenv("to_emails", "test_to_emails")
    monkeypatch.setenv("from_email", "test_from_email")
    monkeypatch.setenv("SENDGRID_API_KEY", "test_key")
    monkeypatch.setenv("template_id", "test_template_id")
    subject = "test_subject"
    task = "test_task"
    deadline = "test_deadline"
    return_client_mock = mocker.Mock()
    api_client_mock = mocker.patch(
        "send_grid_python.outbound_email.SendGridAPIClient",
        return_value=return_client_mock,
    )
    message_mock = mocker.Mock()
    mail_mock = mocker.patch(
        "send_grid_python.outbound_email.Mail",
        return_value=message_mock,
    )

    send_email_message(
        subject=subject,
        task=task,
        deadline=deadline,
        to_emails=["to_email"],
        from_email="from_email",
    )

    mail_mock.assert_called_once_with(from_email="from_email", to_emails=["to_email"])
    assert message_mock.template_id == "test_template_id"
    assert message_mock.dynamic_template_data == {
        "subject": subject,
        "task": task,
        "deadline": deadline,
    }
    api_client_mock.assert_called_once_with(api_key="test_key")
    return_client_mock.send.assert_called_once_with(message=message_mock)


def test_send_email_message_throws_error(mocker, caplog, monkeypatch) -> None:
    """Test send_email_message when fails."""
    monkeypatch.setenv("to_emails", "test_to_emails")
    monkeypatch.setenv("from_email", "test_from_email")
    monkeypatch.setenv("SENDGRID_API_KEY", "test_key")
    monkeypatch.setenv("template_id", "test_template_id")
    subject = "test_subject"
    task = "test_task"
    deadline = "test_deadline"
    return_client_mock = mocker.Mock()
    mocker.patch(
        "send_grid_python.outbound_email.SendGridAPIClient",
        return_value=return_client_mock,
    )
    return_client_mock.send.side_effect = Exception
    expected_log = "There was an error sending email via SendGrid API"

    with pytest.raises(Exception):
        send_email_message(
            subject=subject,
            task=task,
            deadline=deadline,
        )
    assert expected_log in caplog.text
