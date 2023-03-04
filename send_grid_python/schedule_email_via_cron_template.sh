#!/bin/zsh
<python.exe location> <root_dir>/task_email_alerts/main.py --subject <email subject> --task <task info> \
--deadline <task deadline> (--from_email <from_email> --to_emails <to_emails>) >log 2>error

# note: ( ) means optional
