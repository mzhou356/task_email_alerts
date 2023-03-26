# task_email_alerts
This personal project is to leverage SendGrid and Airflow EmailOperator to send automatic email reminders for various personal appointments.


# SendGrid as SMTP relay
In this project, we use [SendGrid](https://sendgrid.com/) as a SMTP relay to send alert emails.   
   * We will use their [python3 API](https://github.com/sendgrid/sendgrid-python) and APIKEY to send email alert programmatically as an initial set up option.
   * We will also use SendGrid as a SMTP server and integrate it with Airflow to send reminders: [code](https://github.com/mzhou356/task_email_alerts/tree/main/airflow_setup)

# Different ways 
