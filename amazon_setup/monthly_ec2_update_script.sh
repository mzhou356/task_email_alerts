#!/bin/zsh

ec2_instance_id=$(aws ec2 describe-instances --filters Name=instance-state-name,Values=running \
--query 'Reservations[*].Instances[*].[InstanceId]' \
--output text)

aws ec2 terminate-instances --instance-ids "$ec2_instance_id"
