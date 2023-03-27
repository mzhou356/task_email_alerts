# task_email_alerts
This project is to leverage SendGrid, Airflow EmailOperator and AWS tools to send automatic email reminders for various personal appointments.


# SendGrid as SMTP relay
In this project, we use [SendGrid](https://sendgrid.com/) as a SMTP relay to send alert emails.
   * We will use their [python3 API](https://github.com/sendgrid/sendgrid-python) and APIKEY to send email alert programmatically as an initial set up option.
   * We will also use SendGrid as a SMTP server and integrate it with Airflow to send reminders: [code](https://github.com/mzhou356/task_email_alerts/tree/main/airflow_setup)
       * Airflow docker requires min 4G RAM while the ec2 instance I reserved only has 1 G so this plan didn't work out.


# Final Solution
### AWS Setup:
  * EC2 t3 micro (I prepaid for this already) with crontab setup.
      * The crontab calls the main function from the send_grid_python API: [sample_code](https://github.com/mzhou356/task_email_alerts/blob/main/send_grid_python/schedule_email_via_cron_template.sh)
  * We used cloudformation to update the ec2 instance monthly to ensure we have the latest hardware and AMI image from Amazon: [shell_scripts](https://github.com/mzhou356/task_email_alerts/blob/main/amazon_setup/update_monthly_ec2_instances_via_cloudformation.sh).
      * cloud formation template: [template](https://github.com/mzhou356/task_email_alerts/blob/main/amazon_setup/ec2_cloud_formation_sample_tempate.yaml)

      * To create ec2 service role to access 3: [script](https://github.com/mzhou356/task_email_alerts/blob/main/amazon_setup/ec2S3ReadAccessRole.sh)

      * trust policy: [json](https://github.com/mzhou356/task_email_alerts/blob/main/amazon_setup/ec2S3AccessRole-Trust-Policy.json)

      * Initial setup script:
          * [s3_bucket](https://github.com/mzhou356/task_email_alerts/blob/main/amazon_setup/s3_setup.sh)

   * Key steps:
      1. Use the s3 setup script to transfer needed files to the s3 bucket of your choice:
          * cron file: contains all of reminders you want to send via emails with the right schedule intervals.
          * requirements.txt
          * main.py
          * send_grid_python code
      2. Assign the proper role to allow ec2 service to access the s3 bucket.
      3. Set up the cloud formation template and upload to the s3 bucket for cloudformation.
      4. use the shell scripts to delete the cloudformation stack and recreate the cloudformation stack.
