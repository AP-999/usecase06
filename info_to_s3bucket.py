import boto3
import json


def lambda_handler(event, context):
    # Initialize the EC2 client for the Frankfurt (eu-central-1) region and S3 client
    ec2_client = boto3.client('ec2', region_name='eu-central-1')
    s3 = boto3.client('s3', region_name='eu-central-1')

    # Retrieve the details of all EBS volumes in the region
    volumes = ec2_client.describe_volumes()
    total_volumes_size_gb = sum(vol['Size'] for vol in volumes['Volumes'])
    total_volumes_count = len(volumes['Volumes'])

    # Retrieve the details of all EBS snapshots in the region
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
    total_snapshots_size_gb = sum(snap['VolumeSize']
                                  for snap in snapshots['Snapshots'])
    total_snapshots_count = len(snapshots['Snapshots'])

    # Prepare the results for storage
    data = {
        'EBS_Volumes_Count': total_volumes_count,
        'EBS_Volumes_Total_Size_GB': total_volumes_size_gb,
        'EBS_Snapshots_Count': total_snapshots_count,
        'EBS_Snapshots_Total_Size_GB': total_snapshots_size_gb
    }

    # Print the results
    print(data)

    # Upload the data to S3 in a file named ebs_data.json
    s3.put_object(
        Bucket='s3-usecase06',
        Key='ebs_data.json',
        Body=json.dumps(data),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': 'EBS details retrieved and stored in s3-usecase06/ebs_data.json'
    }
