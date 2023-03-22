#!/bin/zsh

# This script contains all boostrap script needed for ec2

sudo yum update -y
sudo amazon-linux-extras install python3.8
python3.8 get-pip.py --user
mkdir task_email_alerts
cd task_email_alerts
aws s3 cp s3://<bucket-name>/send_grid_python send_grid_python --recursive
aws s3 cp s3://<bucket-name>/main.py main.py
aws s3 cp s3://<bucket-name>/requirements.txt requirements.txt
cd ~
aws s3 cp s3://task-alerts/cron_file_info.txt cron_file_info.txt
cd task_email_alerts
python3.8 -m venv email_alert_env
source email_alert_env/bin/activate
pip install -r requirements.txt
cd ~
crontab -l | cat cron_file_info.txt | crontab -
