#!/bin/bash
SECURITY_GROUP_NAME="default"
SECURITY_GROUP_ID=$(aws ec2 describe-security-groups --query "SecurityGroups[?GroupName=='$SECURITY_GROUP_NAME'].[GroupId]" --output text)
echo "SECURITY_GROUP_ID value is $SECURITY_GROUP_ID"
for i in $(cat inbound_rules.csv);
do
    INBOUND_IP=$(echo $i | awk -F, '{ print $1}')
    INBOUND_PORT=$(echo $i | awk -F, '{ print $2}')
    echo "Inbound ip is $INBOUND_IP"
    echo "Inbound port is $INBOUND_PORT"
    aws ec2 authorize-security-group-ingress --protocol tcp --port $INBOUND_PORT --cidr $INBOUND_IP --group-id $SECURITY_GROUP_ID
done