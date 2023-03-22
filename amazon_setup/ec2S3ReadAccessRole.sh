#!/bin/zsh

aws iam create-role --role-name ec2S3AccessRole --assume-role-policy-document file://ec2S3AccessRole-Trust-Policy.json
aws iam attach-role-policy --role-name ec2S3AccessRole --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
aws iam create-instance-profile --instance-profile-name ec2S3AccessRole-Instance-Profile
aws iam add-role-to-instance-profile --role-name ec2S3AccessRole \
--instance-profile-name ec2S3AccessRole-Instance-Profile
aws ec2 associate-iam-instance-profile --instance-id <ec2instanceid> \
--iam-instance-profile Name=ec2S3AccessRole-Instance-Profile
aws ec2 describe-iam-instance-profile-associations  # only to check for associations
