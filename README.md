Step-by-Step Execution Plan
Step 1: Prepare Your AWS Resources

 Launch an EC2 instance (if not already running)
 Create a new EBS volume and attach it to the instance (if needed)
 Take a manual snapshot of that volume

Note down:

Snapshot ID → snap-005219d56922a25ef
Availability Zone → us-west-2b

Step 2: Create an IAM Role for Lambda
Go to IAM > Roles > Create Role=AmazonEC2FullAccess

Select AWS service > Lambda

Attach these policies:
AmazonEC2FullAccess 
Name it: lambda-ec2-snapshot-role

Step 3: Create the Lambda Function
Go to Lambda > Create Function

Runtime: Python 3.12

Name: restoreEC2fromSnapshot

Execution Role: Select the IAM role created in Step 2

Step 4: Paste the Python Code
Click Deploy

Step 5: Create and Run Test Event
Click Test > Configure test event

Name it: kp-manual-test

Click Test

If successful, you’ll see:

Volume created from snapshot
Instance launched
Volume attached as /dev/sdf

Sometimes it fails with timeout error

then
Step 6: Increase Lambda Timeout
Go to lamda > Configuration > General Configuration

Click Edit>Change timeout from 3 seconds to 2 minutes

Save

Deploy and test again
