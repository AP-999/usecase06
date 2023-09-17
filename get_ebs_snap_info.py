import boto3

def lambda_handler(event, context):
    # Initialize the EC2 client for the Frankfurt (eu-central-1) region
    ec2_client = boto3.client('ec2', region_name='eu-central-1')

    # Retrieve the details of all EBS volumes in the region
    volumes = ec2_client.describe_volumes()
    total_volumes_size_gb = sum(vol['Size'] for vol in volumes['Volumes'])
    total_volumes_count = len(volumes['Volumes'])

    # Retrieve the details of all EBS snapshots in the region
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
    total_snapshots_size_gb = sum(snap['VolumeSize'] for snap in snapshots['Snapshots'])
    total_snapshots_count = len(snapshots['Snapshots'])

    # Print the results
    print(f"Number of EBS Volumes in Frankfurt: {total_volumes_count}")
    print(f"Overall size of EBS Volumes in Frankfurt: {total_volumes_size_gb} GB")
    print(f"Number of EBS Snapshots in Frankfurt: {total_snapshots_count}")
    print(f"Overall size of EBS Snapshots in Frankfurt: {total_snapshots_size_gb} GB")

    return {
        'statusCode': 200,
        'body': 'Details retrieved and printed. Check Lambda logs.'
    }
