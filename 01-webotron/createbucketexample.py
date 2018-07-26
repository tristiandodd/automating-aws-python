# coding: utf-8
import boto3 #imports boto
session = boto3.Session(profile_name='pythonAutomation') #Name you use with Aws configure
s3 = session.resource('s3') #Sets S3 to the AWS resource S3
for bucket in s3.buckets.all():
    print(bucket) #Returns all the buckets associated with the Profile
#Creates a new bucket
new_bucket = s3.create_bucket(
    Bucket='pythonautomation-tristian', #BucketName(Must be specific and no capital letters)
    CreateBucketConfiguration={
    'LocationConstraint': 'us-east-2'}) #Sets the Location of the bucket!

for bucket in s3.buckets.all():
    print(bucket)   #Returns the buckets after the new one has been created
