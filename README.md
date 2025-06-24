**Assignment 17: Restore EC2 Instance from Snapshot using AWS Lambda**



 Prerequisites:

* AWS account with EC2 and Lambda permissions
* One existing snapshot (`snap-005219d56922a25ef`) in Availability Zone `us-west-2b`
* An existing AMI to launch EC2 (`ami-05f991c49d264708f`)

---

###  Lambda Function Summary

This Lambda function:

1. Creates a new EBS volume from a specific snapshot
2. Launches a new EC2 instance
3. Attaches the new volume to the instance as a secondary volume

---

###  Configuration:

**Lambda Runtime**: Python 3.12
**IAM Role Permissions**:
Ec2 full access

###  Execution Results:

* Lambda tested successfully after increasing timeout
* Volume created and attached from snapshot
* New EC2 instance launched

---

###

* The volume is attached as a secondary device (`/dev/sdf`)
* This allows access to the snapshot data inside the new EC2


