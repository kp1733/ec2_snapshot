# Assignment 17: Restore EC2 from Snapshot using AWS Lambda

## Objective
Automate the restoration of an EC2 instance from a pre-created snapshot using a Lambda function.

## Steps Followed

### 1. Created AWS Resources
- EC2 instance and EBS volume created.
- Snapshot taken from the volume: `snap-005219d56922a25ef`

### 2. IAM Role
- Created a role with EC2 full access for Lambda.

### 3. Created Lambda Function
- Language: Python 3.12
- Increased timeout to 2 minutes
- Deployed the final code.

### 4. Lambda Logic
- Create volume from snapshot
- Launch EC2
- Attach volume to instance

### 5. Triggered Lambda
- Manually via test event
- Also configured a daily EventBridge schedule (optional)

### 6. Validation
- Verified EC2 launched
- Verified volume attached

## Screenshots
- ![Lambda config](screenshots/lambda_config.png)
- ![IAM Role](screenshots/iam_role.png)
- ![Test Success](screenshots/test_success.png)
- ![EventBridge](screenshots/event_trigger.png)

## Final Code File
See `lambda_function.py` in this repo.

## Status
 Task completed successfully
