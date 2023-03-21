#!/bin/zsh

# This script contains all boostrap script needed for ec2

sudo yum update -y
mkdir task_email_alerts
cd task_email_alerts
sudo amazon-linux-extras install python3.8
python3.8 get-pip.py --user
python3.8 -m venv email_alert_env
source email_alert_env/bin/activate
pip install -r requirements.txt
cd
crontab -l | cat cron_file_copy.txt | crontab -
