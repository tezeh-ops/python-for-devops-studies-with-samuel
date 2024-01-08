
import boto3  

client = boto3.client('s3')  # this is a common syntax foe Aws all we need ti do is the channge the client we want to talk to e.g ('s3') or ('Ec2') or ('Eks') ...

response = client.create_bucket(
    
    Bucket='sam-demo-boto3-tz-97',
    
)

print(response)