import boto3
 
def create_s3_bucket(bucket_name, region='us-east-1'):
  """Creates an S3 bucket in the specified region.
 
  Args:
    bucket_name: The name of the S3 bucket to create.
    region: The AWS region where the bucket should be created. Defaults to 'us-east-1'.
  """
 
  s3 = boto3.client('s3')
  try:
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
    print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
  except Exception as e:
    print(f"Error creating S3 bucket: {e}")
 
if __name__ == "__main__":
  bucket_name = 'my-new-bucket'  # Replace with your desired bucket name
  region = 'us-east-1'  # Replace with your desired region
 
  create_s3_bucket(bucket_name, region)