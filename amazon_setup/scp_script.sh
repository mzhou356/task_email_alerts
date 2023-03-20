#!/bin/zsh

# This shell script will scp needed python modules from local machine to aws EC2 linux ami

scp -r "$HOME"/Documents/projects/task_email_alerts/send_grid_python ec2-user@scheduler.mindy-dossett.com:task_email_alerts/send_grid_python
scp "$HOME"/Documents/projects/task_email_alerts/main.py ec2-user@scheduler.mindy-dossett.com:task_email_alerts/main.py
