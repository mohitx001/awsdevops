import os,json,boto3

s3 = boto3.client("s3")
sns = boto3.client("sns")

def lambda_handler(event,context):
    print(event)
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    aws_region = event['Records'][0]['awsRegion']
    key_val = event['Records'][0]['s3']['object']['key']
    size_val = event['Records'][0]['s3']['object']['size']/1024
    ipAddress = event['Records'][0]['requestParameters']['sourceIPAddress']
    event_time = event['Records'][0]['eventTime']

    message = "Hi, \n The Event time is : " + event_time + "Hi, \nYou are receiving this email because you are subscribed to this S3event. \nThe Source Bucket is : " + source_bucket + "\nThe AWS Region is :" + aws_region + "\nThe Uploaded Filename is : " + key_val + " having Size : " + str(size_val) + " KB" + "\nThe Object is upload from IP Address: " + ipAddress
    #Below are the variables for copy_object function parameters
    #Provide below the target bucket name where your object needs to be copied
    backupBucket = os.environ['BACKUP_BUCKET_NAME']
    snsArn = os.environ['SNS_TOPIC_ARN']
    emailSubject = "S3EventTrigger-Notification"
    copy_source = {'Bucket' : source_bucket, 'Key' : key_val}
    sns_response = sns.publish(TopicArn=snsArn,Message=message,Subject=emailSubject)
    print(sns_response)
    try:
        print("Copying the object from source to destination")
        s3.copy_object(Bucket=backupBucket,Key=key_val, CopySource=copy_source)
    except Exception as e:
        print(e)
        print("Error getting object")
        raise e