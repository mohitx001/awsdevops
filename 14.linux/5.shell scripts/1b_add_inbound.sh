# This Script will take command line arguments for Security Group Name, CSV File Path, AWS Region Name where the Security Group is present.
# bash 1b_add_inbound.sh default input_rules.csv us-east-1
# bash 1b_add_inbound.sh default-sg input_rules.csv ap-south-1
# bash 1b_add_inbound.sh default input_rules.csv us-east-2
#!/bin/bash
SECURITY_GROUP_NAME=$1
INPUT_FILE_NAME=$2
REGION_NAME=$3
SECURITY_GROUP_ID=$(aws ec2 describe-security-groups --region $REGION_NAME --query "SecurityGroups[?GroupName=='$SECURITY_GROUP_NAME'].[GroupId]" --output text)
echo "SECURITY_GROUP_ID value is $SECURITY_GROUP_ID --region $REGION_NAME"
if [ $SECURITY_GROUP_ID != "" ]; then
    if [ -f $INPUT_FILE_NAME ]; then
        for i in $(cat $INPUT_FILE_NAME);
        do
            INBOUND_IP=$(echo $i | awk -F, '{ print $1}')
            INBOUND_PORT=$(echo $i | awk -F, '{ print $2}')
            echo "Inbound ip is $INBOUND_IP"
            echo "Inbound port is $INBOUND_PORT"
            aws ec2 authorize-security-group-ingress --region $REGION_NAME --protocol tcp --port $INBOUND_PORT --cidr $INBOUND_IP --group-id $SECURITY_GROUP_ID
        done
    else
        echo "File $INPUT_FILE_NAME does not exists"
    fi
else
    echo "$SECURITY_GROUP_ID is blank, cannot execute"
fi