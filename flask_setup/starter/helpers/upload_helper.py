import boto3
import os
import random
import string

session = boto3.session.Session()
client = session.client(
    's3',
    region_name=os.environ.get('SPACE_REGION'),
    endpoint_url=os.environ.get('SPACE_ENDPOINT'),
    aws_access_key_id=os.environ.get('SPACE_KEY'),
    aws_secret_access_key=os.environ.get('SPACE_SECRET'))

def do_upload(file_to_upload):
    try:
        # create file name
        name = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '.' + file_to_upload.filename.split('.')[-1]
        # upload file
        client.upload_fileobj(file_to_upload, os.environ.get('SPACE_NAME'), name, ExtraArgs={'ACL': 'public-read'})
        return f"{os.environ.get('SPACE_EDGE_ENDPOINT')}/{os.environ.get('SPACE_NAME')}/{name}"
    except Exception as e:
        print(e)
        return None

def remove_upload(file_to_remove):
    try:
        client.delete_object(Bucket=os.environ.get('SPACE_NAME'), Key=file_to_remove)
        return True
    except Exception as e:
        print(e)
        return None