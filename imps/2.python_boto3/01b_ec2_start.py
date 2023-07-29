# This function is written to get list of EC2 instances that are in 'stopped' state and start them.

import boto3
ec2 = boto3.client('ec2')

ec2_dict=ec2.describe_instances()
print("ec2_dict type is",type(ec2_dict))
print("ec2_dict is",ec2_dict)
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
	print("instance_id is",instance_id)
	print("instance_state is",instance_state)
	InstanceIdsList= []
	if instance_state == 'stopped':
		print(instance_id ,"will be started")
		InstanceIdsList.append(instance_id)
		ec2.start_instances(InstanceIds=InstanceIdsList)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances
# Below is the Example Python Dictionary response for 'ec2.describe_instances()'
'''
{
	'Reservations': [{
		'Groups': [],
		'Instances': [{
			'AmiLaunchIndex': 0,
			'ImageId': 'ami-08f63db601b82ff5f',
			'InstanceId': 'i-0f998cd8f0c4d7765',
			'InstanceType': 't2.micro',
			'KeyName': 'aws-linux-mumbai',
			'LaunchTime': datetime.datetime(2020, 12, 13, 3, 54, 1, tzinfo = tzlocal()),
			'Monitoring': {
				'State': 'disabled'
			},
			'Placement': {
				'AvailabilityZone': 'ap-south-1a',
				'GroupName': '',
				'Tenancy': 'default'
			},
			'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
			'PrivateIpAddress': '172.31.29.10',
			'ProductCodes': [],
			'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
			'PublicIpAddress': '13.233.149.161',
			'State': {
				'Code': 16,
				'Name': 'running'
			},
			'StateTransitionReason': '',
			'SubnetId': 'subnet-763c651f',
			'VpcId': 'vpc-b680d3df',
			'Architecture': 'x86_64',
			'BlockDeviceMappings': [{
				'DeviceName': '/dev/xvda',
				'Ebs': {
					'AttachTime': datetime.datetime(2020, 12, 5, 4, 24, 8, tzinfo = tzlocal()),
					'DeleteOnTermination': True,
					'Status': 'attached',
					'VolumeId': 'vol-00b0cc9a7fbefa94c'
				}
			}],
			'ClientToken': '',
			'EbsOptimized': False,
			'EnaSupport': True,
			'Hypervisor': 'xen',
			'IamInstanceProfile': {
				'Arn': 'arn:aws:iam::082123755555:instance-profile/EC2-AWS-CICD-Roile',
				'Id': 'AIPARGTVDL3VW3O4VSDK6'
			},
			'NetworkInterfaces': [{
				'Association': {
					'IpOwnerId': 'amazon',
					'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
					'PublicIp': '13.233.149.161'
				},
				'Attachment': {
					'AttachTime': datetime.datetime(2020, 12, 5, 4, 24, 7, tzinfo = tzlocal()),
					'AttachmentId': 'eni-attach-08cfd5390b05b478a',
					'DeleteOnTermination': True,
					'DeviceIndex': 0,
					'Status': 'attached'
				},
				'Description': '',
				'Groups': [{
					'GroupName': 'launch-wizard-2',
					'GroupId': 'sg-068aab378fd4baf27'
				}],
				'Ipv6Addresses': [],
				'MacAddress': '02:ce:d0:5a:79:d0',
				'NetworkInterfaceId': 'eni-0d047c9183d815761',
				'OwnerId': '082666708139',
				'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
				'PrivateIpAddress': '172.31.29.10',
				'PrivateIpAddresses': [{
					'Association': {
						'IpOwnerId': 'amazon',
						'PublicDnsName': 'ec2-13-233-149-161.ap-south-1.compute.amazonaws.com',
						'PublicIp': '13.233.149.161'
					},
					'Primary': True,
					'PrivateDnsName': 'ip-172-31-29-10.ap-south-1.compute.internal',
					'PrivateIpAddress': '172.31.29.10'
				}],
				'SourceDestCheck': True,
				'Status': 'in-use',
				'SubnetId': 'subnet-763c651f',
				'VpcId': 'vpc-b680d3df',
				'InterfaceType': 'interface'
			}],
			'RootDeviceName': '/dev/xvda',
			'RootDeviceType': 'ebs',
			'SecurityGroups': [{
				'GroupName': 'launch-wizard-2',
				'GroupId': 'sg-068aab378fd4baf27'
			}],
			'SourceDestCheck': True,
			'Tags': [{
				'Key': 'Name',
				'Value': 'EC2-A'
			}],
			'VirtualizationType': 'hvm',
			'CpuOptions': {
				'CoreCount': 1,
				'ThreadsPerCore': 1
			},
			'CapacityReservationSpecification': {
				'CapacityReservationPreference': 'open'
			},
			'HibernationOptions': {
				'Configured': False
			},
			'MetadataOptions': {
				'State': 'applied',
				'HttpTokens': 'optional',
				'HttpPutResponseHopLimit': 1,
				'HttpEndpoint': 'enabled'
			},
			'EnclaveOptions': {
				'Enabled': False
			}
		}],
		'OwnerId': '082666708139',
		'ReservationId': 'r-00b4fb251f781e276'
	}, {
		'Groups': [],
		'Instances': [{
			'AmiLaunchIndex': 0,
			'ImageId': 'ami-08f63db601b82ff5f',
			'InstanceId': 'i-0b61f89ca75f611a8',
			'InstanceType': 't2.micro',
			'KeyName': 'aws-linux-mumbai',
			'LaunchTime': datetime.datetime(2020, 12, 6, 4, 2, 16, tzinfo = tzlocal()),
			'Monitoring': {
				'State': 'disabled'
			},
			'Placement': {
				'AvailabilityZone': 'ap-south-1a',
				'GroupName': '',
				'Tenancy': 'default'
			},
			'PrivateDnsName': 'ip-172-31-29-8.ap-south-1.compute.internal',
			'PrivateIpAddress': '172.31.29.8',
			'ProductCodes': [],
			'PublicDnsName': '',
			'State': {
				'Code': 80,
				'Name': 'stopped'
			},
			'StateTransitionReason': 'User initiated (2020-12-06 08:09:44 GMT)',
			'SubnetId': 'subnet-763c651f',
			'VpcId': 'vpc-b680d3df',
			'Architecture': 'x86_64',
			'BlockDeviceMappings': [{
				'DeviceName': '/dev/xvda',
				'Ebs': {
					'AttachTime': datetime.datetime(2020, 12, 6, 4, 2, 17, tzinfo = tzlocal()),
					'DeleteOnTermination': True,
					'Status': 'attached',
					'VolumeId': 'vol-0cd59e4a44b40514a'
				}
			}],
			'ClientToken': '',
			'EbsOptimized': False,
			'EnaSupport': True,
			'Hypervisor': 'xen',
			'NetworkInterfaces': [{
				'Attachment': {
					'AttachTime': datetime.datetime(2020, 12, 6, 4, 2, 16, tzinfo = tzlocal()),
					'AttachmentId': 'eni-attach-0a2f1cc00508a6fcb',
					'DeleteOnTermination': True,
					'DeviceIndex': 0,
					'Status': 'attached'
				},
				'Description': '',
				'Groups': [{
					'GroupName': 'launch-wizard-2',
					'GroupId': 'sg-068aab378fd4baf27'
				}],
				'Ipv6Addresses': [],
				'MacAddress': '02:91:ff:b3:66:54',
				'NetworkInterfaceId': 'eni-0543adad2f9a9dbe7',
				'OwnerId': '082666708139',
				'PrivateDnsName': 'ip-172-31-29-8.ap-south-1.compute.internal',
				'PrivateIpAddress': '172.31.29.8',
				'PrivateIpAddresses': [{
					'Primary': True,
					'PrivateDnsName': 'ip-172-31-29-8.ap-south-1.compute.internal',
					'PrivateIpAddress': '172.31.29.8'
				}],
				'SourceDestCheck': True,
				'Status': 'in-use',
				'SubnetId': 'subnet-763c651f',
				'VpcId': 'vpc-b680d3df',
				'InterfaceType': 'interface'
			}],
			'RootDeviceName': '/dev/xvda',
			'RootDeviceType': 'ebs',
			'SecurityGroups': [{
				'GroupName': 'launch-wizard-2',
				'GroupId': 'sg-068aab378fd4baf27'
			}],
			'SourceDestCheck': True,
			'StateReason': {
				'Code': 'Client.UserInitiatedShutdown',
				'Message': 'Client.UserInitiatedShutdown: User initiated shutdown'
			},
			'Tags': [{
				'Key': 'Name',
				'Value': 'EC2-B'
			}],
			'VirtualizationType': 'hvm',
			'CpuOptions': {
				'CoreCount': 1,
				'ThreadsPerCore': 1
			},
			'CapacityReservationSpecification': {
				'CapacityReservationPreference': 'open'
			},
			'HibernationOptions': {
				'Configured': False
			},
			'MetadataOptions': {
				'State': 'applied',
				'HttpTokens': 'optional',
				'HttpPutResponseHopLimit': 1,
				'HttpEndpoint': 'enabled'
			},
			'EnclaveOptions': {
				'Enabled': False
			}
		}],
		'OwnerId': '082666708139',
		'ReservationId': 'r-00bab1d33b9544936'
	}],
	'ResponseMetadata': {
		'RequestId': '1d003b2f-5fad-4e8c-ada7-e7ca2a33fb1d',
		'HTTPStatusCode': 200,
		'HTTPHeaders': {
			'x-amzn-requestid': '1d003b2f-5fad-4e8c-ada7-e7ca2a33fb1d',
			'content-type': 'text/xml;charset=UTF-8',
			'transfer-encoding': 'chunked',
			'vary': 'accept-encoding',
			'date': 'Sun, 13 Dec 2020 05:52:52 GMT',
			'server': 'AmazonEC2'
		},
		'RetryAttempts': 0
	}
}

'''
