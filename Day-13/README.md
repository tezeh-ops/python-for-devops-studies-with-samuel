Next Let try to see how we can list the ACL of the Bucket we just created ==
```
import boto3
client = boto3.client('s3')
response = client.create_bucket(
    
    Bucket='sam-demo-boto3-tz-97',
    
)
print(response)   # The response will give us an output details on the bucket we just create
```
===========================>

LET do a [project using Lambda to handle Cost optimization in AWS ];
> Question why use boto3?  we use boto3 to  create resources on AWS using python. 
What is the the differences using ; 
- AWS CLI: Use it for simple and shot task 
- ClouldFromation  and Terraform : we use them in create thing reusable template for our resourses
- Boto3: boto3 is simple a script we write in python to manage or create resources on AWS and it common importance above using  AWS CLI due to the Serverless resourse in AWS like Lambda  and the rest where AWS CLI can't be use.
> AWS  LAMBDA
As a DevOps engineer  Lambda  Function is most learn service due to which we cant use it manage:
- Cost optimization
- We can use it to trigger other service like [ S3,  CloudWatch,  etc]
- Security or Compliance ( here we can restrict what should be create or no to be according the organization specification.
Why Lambda ( what problem is it solving) ?
So when we talk of lambda there TWO  thing that should be at the back of our mind:
1. Compute ( it can act just as EC2)
2. Serverless. 
So  lambda belongs to this two families [ compute/serverless]
Different Between Lambda and EC2
> With Ec2  we are responsible in setting up the server and tearing it down. WHILE with Lambda we not AWS is  Responsible  for the Compute( server) setup and down  and what ever configuration that maybe required E.g CPU, scale up,  Memory  etc  and when is done it will scale everything down. 
Example
Let say there is a platform call Food delivery platform, and with this platform when a user create a request ( he needs  X Y Z food )  and he goes to the checkout and do the payment, and once the transaction is done then he's food other will be placed.  So if we are using Lambda function for this platform we can say when the User sent the Request only then will this application should be run and when the user is done with the payment and everything the AWS will tear down the application.
> So EC2 instance is pay as you Used  WHILE  Lambda is pay only when used.
> Nb when we create an EC2 instance  we will get an IP-address ( public or Private)   WHILE  with Lambda function we don't get anything related to IP-address  and we don't even know where the  computer server are created. 

Question >>.  How will you decide if we should use Lambda ( serverless)  OR  use  EC2 ?  AS a DevOps engineer you will not decide if the project that you are working on because it will be taken care by the Development team / Architectural team. They will decide if the application should go with the < Server approach OR the serverless approach >  which then depends a lot on the application that is written and if it's written in with serverless approach in mind or Not. 

                      Let see how to create a lambda Function. 
> go to the console an search Lambda 
> click on < create function> 
NB > if you want you application inside the Lambda function server to be access from outside we most < Enable Function URL > if not the application will run but we can't access it from outside.
> For those that can access it  if we chose < NONE >  as seen below it means that anyone with the URL can access it  BUT if chose  < AWS_IAM > if will do authentication just to allowed only those authorizes to access it.

>> NB  when we create a function we will see < +Add Trigger >       and      < +Add   destination >  the  < destination> i s mandatory but  the  < trigger > is used most of the time.
>.  And Lambda function are < Event  trigger >   function  and this event can be ( CloudWatch, S3,  EBS,  etc  ....  )  and other services that has the trigger functions ability if not we will Manually Trigger the Lambda function.
>.  NB the default execution time for Lambda function is < 3 seconds >  but we can increase it in the configuration. And when configuring the Time we should keep it as small as we can't Because AWS will charge us base on that too .

                                                                                                
Cloud   Cost Optimization 
1. let see how DevOps/Cloud engineers can optimizes cost in cloud by using the delete function.
- here we will be using the Lambda function to archive this . And inside the Lambda function we will write out python code using the  < Boto3  module > that we talk to the AWS API
                                                                              Project Outline ==

AWS Cloud Cost Optimization - Identifying Stale Resources


Identifying Stale EBS Snapshots

In this example, we'll create a Lambda function that  identifies EBS snapshots that are no longer associated with any active  EC2 instance and deletes them to save on storage costs.

Description:

The Lambda function fetches all EBS snapshots owned by the  same account ('self') and also retrieves a list of active EC2 instances  (running and stopped). For each snapshot, it checks if the associated  volume (if exists) is not associated with any active instance. If it  finds a stale snapshot, it deletes it, effectively optimizing storage  costs.

Solution :
- leg create our Lambda  FUNCTION
- Below  is our python code  copy and paste==
```
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])
    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()
    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')
        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
```
- click deploy and run test [ since we want to test it manually first enter the test name and saved it ]  the run the code .
- here below is the error i got when i run the test code=========

Test Event Name
test

Response
{
  "errorMessage": "An error occurred (UnauthorizedOperation) when calling the DescribeSnapshots operation: You are not authorized to perform this operation.",
  "errorType": "ClientError",
  "requestId": "7dbab330-0823-40e7-95f3-423b1d5abc2e",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 7, in lambda_handler\n    response = ec2.describe_snapshots(OwnerIds=['self'])\n",
    "  File \"/var/lang/lib/python3.11/site-packages/botocore/client.py\", line 534, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/lang/lib/python3.11/site-packages/botocore/client.py\", line 976, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
}
Function Logs
START RequestId: 7dbab330-0823-40e7-95f3-423b1d5abc2e Version: $LATEST
[ERROR] ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeSnapshots operation: You are not authorized to perform this operation.
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 7, in lambda_handler
    response = ec2.describe_snapshots(OwnerIds=['self'])
  File "/var/lang/lib/python3.11/site-packages/botocore/client.py", line 534, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/var/lang/lib/python3.11/site-packages/botocore/client.py", line 976, in _make_api_call
    raise error_class(parsed_response, operation_name)END RequestId: 7dbab330-0823-40e7-95f3-423b1d5abc2e
REPORT RequestId: 7dbab330-0823-40e7-95f3-423b1d5abc2e	Duration: 2508.96 ms	Billed Duration: 2509 ms	Memory Size: 128 MB	Max Memory Used: 88 MB	Init Duration: 254.84 ms

Request ID
7dbab330-0823-40e7-95f3-423b1d5abc2e
======================================================================>>. This due to which we haven't set up the permissions yet:
> go to the configuration  tag on for your  Lambda function,  Then click on  < permission > == then click on the <  role link > provided and add the necessary permisions ==

> the permission  to Add are [ since to fine the permission it may be a little bit challenging so we are going to create the permissions ==
 


> next give the policy a < name > the create it.
> Go back to the link and if the policy we create is not attach already we can now attach it.
- Let go back to our function a run the test on the code again.
- we got and error ===
errorMessage": "An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation.",
  "errorType": "ClientError",
  "requestId": "9f3e739a-eacc-4fe2-ba18-124763a0f63b",   Recuses we didn't give permission to < DescribeInstances > we the permission we created above so let go create another  on for that purpose.  [ Nb we could just grant it now <EC2FullAcess >  but since we want to do just the required privileges we create it as we did above. ] so follow the same procedure. Then search for  < EC2 >  and under  < Actions>  serach for  < DescribeVolume>    & < DescribeInstance > the click < next and give it a name  and create it > 
- let test code again { and is successful } == NB  But the < Snapshot> will not be delete why?  because currently all the Snapshot are associated to an EC2 instance. 
- Let Delete the instance and see what happens .  as we ran the code it delete and EBS Voluem thar i create and did not associate it to an Instance ==


- NEXT our code and lambda function is working good but we are triggering it < Manually > so what can we do to automate the process?
>  We can make use of the CloudWtach. And we can invoke our Function from there and we can tell it invoke this Lambda Function < once a week,  or every month  etc >
> in cloudwatch navigate to  <Event >  then click < Role > then we can configure our  < Lambda Function > as an event or we can still run it manually is up to us to decide.
> Click create Role ==

> next page we can fill out the requirement for the time we want the event to be trigger but due to Cost we will cont configure it for now. ====

========================================The end 
