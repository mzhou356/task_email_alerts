#!/bin/zsh

stack_name=$(aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE \
--query 'StackSummaries[*].[StackName]' --output text)

aws cloudformation delete-stack --stack-name "$stack_name"

echo "wait for $stack_name to be completely deleted."
aws cloudformation wait stack-delete-complete --stack-name "$stack_name"
echo "$stack_name is completely deleted and create a new one."

aws cloudformation create-stack --stack-name "$stack_name" --template-url \
https://cf-templates-dmxir1d884ky-us-east-1.s3.us-east-1.amazonaws.com/ec2_cloud_formation_template.yaml
