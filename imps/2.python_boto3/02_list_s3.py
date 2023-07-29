# Retrieve the list of existing buckets
import boto3
s3 = boto3.client('s3')
bucket_dict=s3.list_buckets()
print("Type of bucket_dict is",type(bucket_dict))
print(bucket_dict)
bucket_list=bucket_dict['Buckets']
print("Type of bucket_list is",type(bucket_list))
for bucket_info in bucket_list:
    print("Type of bucket_info is",type(bucket_info))
    print("Bucket Name is ",bucket_info['Name'])