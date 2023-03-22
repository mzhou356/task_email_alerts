#!/bin/zsh

# shellcheck disable=SC1073
# shellcheck disable=SC1009
aws s3 mb <bucket_name>
aws s3 cp  "$HOME"/Documents/projects/task_email_alerts/send_grid_python \
s3://<bucket_name>/send_grid_python --recursive
aws s3 cp "$HOME"/Documents/projects/task_email_alerts/main.py \
s3://<bucket_name>/main.py
cp "$HOME"/Documents/projects/task_email_alerts/requirements.txt \
s3://<bucket_name>/requirements.txt
aws s3 cp "$HOME"/Documents/projects/task_email_alerts/amazon_setup/cron_file_copy.txt \
s3://<bucket_name>/cron_file_info.txt
