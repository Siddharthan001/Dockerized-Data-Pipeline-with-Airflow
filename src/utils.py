import boto3
import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

def upload_to_s3(file_path, bucket_name, s3_key):
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=config["aws"]["access_key"],
            aws_secret_access_key=config["aws"]["secret_key"]
        )
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Failed to upload to S3: {e}")
