import boto3
client = boto3.client('s3', region_name=us-east-1)
bucketname =  "aws-bigdata-us-east-1"
subfolder1 = test/test1/test2/test3
subfolder2 = npp/npp1/npp2/npp3/npp4
subfolder3 = market/marker1/market2/market3/market4

client.create_bucket(Bucket=bucketname)
client.put_object(Bucket=bucketname,key=subfolder1)
client.put_object(Bucket=bucketname,key=subfolder2)
client.put_object(Bucket=bucketname,key=subfolder3)
