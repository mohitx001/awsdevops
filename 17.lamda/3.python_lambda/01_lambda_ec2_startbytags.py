# This function is written to get list of EC2 instances that are in 'stopped' state and start them.
# Below code can be optimized to first find all the instance id as per Tags and once a List of Instance id is created, can be passed to ec2.start_instances(InstanceIds=InstanceIdsList)
# Execute this code in Lambda Function and also create a Crontab Schedule in CloudWatch Rule by adding Target as the Lambda Function that will execute the code.
# Execution of this code in Lambda should have EC2 List and appropriate Policies to start and stop instances.
# Tag Key = env , Tag Value = dev
# env : dev
# Execution of this code in Lambda should have EC2 List and appropriate Policies to start and stop instances.

import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    ec2_dict=ec2.describe_instances()
    #print("ec2_dict type is",type(ec2_dict))
    #print("ec2_dict is",ec2_dict)
    reservations_list=ec2_dict['Reservations']
    print(reservations_list)
    print(type(reservations_list))
    print(len(reservations_list))
    # print("reservations_list is",reservations_list, type(reservations_list),len(reservations_list))
    print("-----------------------------------------")
    for instances in reservations_list:
        # print("instances",instances,type(instances))
        print("instance is of type",type(instances))
        instance_id=instances['Instances'][0]['InstanceId']
        instance_state=instances['Instances'][0]['State']['Name']
        tags_list=instances['Instances'][0]['Tags']
        print("tags_list is - ", tags_list)
        print("instance_id is",instance_id)
        print("instance_state is",instance_state)
        InstanceIdsList= []
        # [{'Key': 'env', 'Value': 'dev'}, {'Key': 'Name', 'Value': 'EC2-B'}]
        for tags in tags_list:
            print(type(tags))
            if tags['Key'] == 'env' and tags['Value'] == 'dev':
                if instance_state == 'stopped':
                    print(instance_id ,"will be started")
                    InstanceIdsList.append(instance_id)
                    ec2.start_instances(InstanceIds=InstanceIdsList)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }