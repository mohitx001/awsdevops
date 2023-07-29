#!/bin/bash

SDLC_ENVIRONMENT=$1
# REGION_NAME="ap-south-1"
case "$SDLC_ENVIRONMENT" in
  "dev")
      VPC_CIDR="10.192.0.0/16"
      PublicSubnet1CIDR="10.192.1.0/24"
      PublicSubnet2CIDR="10.192.2.0/24"
      PrivateSubnet1CIDR="10.192.3.0/24"
      PrivateSubnet2CIDR="10.192.4.0/24"
      ;;
  "qa")
      VPC_CIDR="10.192.0.0/16"
      PublicSubnet1CIDR="10.192.5.0/24"
      PublicSubnet2CIDR="10.192.6.0/24"
      PrivateSubnet1CIDR="10.192.7.0/24"
      PrivateSubnet2CIDR="10.192.8.0/24"
      ;;
  "prod")
      VPC_CIDR="10.192.0.0/16"
      PublicSubnet1CIDR="10.192.9.0/24"
      PublicSubnet2CIDR="10.192.10.0/24"
      PrivateSubnet1CIDR="10.192.11.0/24"
      PrivateSubnet2CIDR="10.192.12.0/24"
      ;;
  "infra")
      VPC_CIDR="10.192.0.0/16"
      PublicSubnet1CIDR="10.192.13.0/24"
      PublicSubnet2CIDR="10.192.14.0/24"
      PrivateSubnet1CIDR="10.192.15.0/24"
      PrivateSubnet2CIDR="10.192.16.0/24"
      ;;
  "")
    echo "Value is not in ''"
      ;;
esac
bash 04_case.sh ${SDLC_ENVIRONMENT}

echo "Value of VPC_CIDR ${VPC_CIDR}"
echo "Value of PublicSubnet1CIDR ${PublicSubnet1CIDR}"
echo "Value of PublicSubnet2CIDR ${PublicSubnet2CIDR}"
echo "Value of PrivateSubnet1CIDR ${PrivateSubnet1CIDR}"
echo "Value of PrivateSubnet2CIDR ${PrivateSubnet2CIDR}"

# --parameter-overrides : key in the below command is the Paramter Name in CF template, and value of this key is the Shell Variable
aws cloudformation deploy --template-file templates/network_resources.yml --stack-name $SDLC_ENVIRONMENT-network-stack --parameter-overrides EnvironmentName=$SDLC_ENVIRONMENT VpcCIDR=${VPC_CIDR} PublicSubnet1CIDR=${PublicSubnet1CIDR} PublicSubnet2CIDR=${PublicSubnet2CIDR} PrivateSubnet1CIDR=${PrivateSubnet1CIDR} PrivateSubnet2CIDR=${PrivateSubnet2CIDR} --region ${REGION_NAME}