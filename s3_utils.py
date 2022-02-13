import boto3
from botocore.client import Config
# S3 Connect


ACCESS_KEY_ID = 'AKIAVJLRI6OJEKXXXXX'
ACCESS_SECRET_KEY = 'XXXXXX/hkFrK8LXXXXx/Z5vuuTpGGD9tnXXXXX'
BUCKET_NAME = 'your_s3_bucket_name'


s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    #config=Config(signature_version='s3v4')
)

class s3_File:

    def __init__(self):
        self.BUCKET_NAME = BUCKET_NAME

    def download(self,f_name,file_location):
        try:
            s3.Bucket(BUCKET_NAME).download_file(f_name, file_location);  # Change the second part
        except Exception as e14:
            file_utils.log_errors("E14|s3utils:download|%s| %s" % (str(e14), file_location))

    def filesize(self,f_name):
        print("Size = ")

