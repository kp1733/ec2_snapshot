# lambda_function.py
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    availability_zone = 'us-west-2b'
    snapshot_id = 'snap-005219d56922a25ef'

    new_volume = ec2.create_volume(
        SnapshotId=snapshot_id,
        AvailabilityZone=availability_zone,
        VolumeType='gp2'
    )

    volume_id = new_volume['VolumeId']
    ec2.get_waiter('volume_available').wait(VolumeIds=[volume_id])

    image_id = 'ami-05f991c49d264708f'
    new_instance = ec2.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        Placement={'AvailabilityZone': availability_zone}
    )

    instance_id = new_instance['Instances'][0]['InstanceId']
    ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

    ec2.attach_volume(
        VolumeId=volume_id,
        InstanceId=instance_id,
        Device='/dev/sdf'
    )

    return {
        'status': 'success',
        'instance_id': instance_id,
        'volume_id': volume_id
    }
