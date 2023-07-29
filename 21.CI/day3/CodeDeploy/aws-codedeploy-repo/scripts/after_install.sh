#!/bin/bash
#accessing instance metadata
EC2_INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
EC2_AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
AMI_ID=$(curl -s http://169.254.169.254/latest/meta-data/ami-id)
PUBLIC_IPV4=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)
#Accessing envrionment variables
sed -i "s/was deployed/was deployed using AWS CodeDeploy on $EC2_INSTANCE_ID in $EC2_AZ having image $AMI_ID with public IP $PUBLIC_IPV4 having application name $APPLICATION_NAME with Deployment Group $DEPLOYMENT_GROUP_NAME and Deployment ID $DEPLOYMENT_ID updated in develop/g" /var/www/html/index.html