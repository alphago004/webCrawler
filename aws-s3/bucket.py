import boto3
import logging
import os

#reading the existing buckets
def list_bucket():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            print ("Bucket exists. The list of buckets are:")
            for bucket in response['Buckets']:
                print(f'Bucket: {bucket["Name"]}')

    except Exception as e:
        logging.error(e)
        return False
    return True

list_bucket()

## Create AWS S3 bucket using python boto3
def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except Exception as e:
        logging.error(e)
        return False
    return True


# Upload a file from local system.
def upload_file(file_name, bucket, object_name=None):   ## change the file path and bucket name fethed from the frontend -> fetch from the frontend form
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

'''
## Calling Create Bucket
result_create = create_bucket("crawler-bucket-1234")   ## need to insert the bucket name which you want to create -> fetch from the frontend   
if result_create :
    print("bucket got created successfully..!")
else:
    print("bucket got created failed..!")
'''


'''
## Uploading a file to bucket
result_upload = upload_file("F:\\RekhuAll\\AzurePoC\\0C7A2552.JPG", "crawler-bucket-1234", "0C7A2552.JPG")   ## need to change the file path and bucket name fethed from the frontend -> fetch from the frontend form

if result_upload :
    print("bucket file uploaded successfully..!")
else:
    print("bucket file upload failed..!")
'''