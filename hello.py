import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 's3-usecase06'
    file_name = 'hello.txt'
    content = 'Hello World!'

    response = s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=content,
        ContentType='text/plain'
    )

    return {
        'statusCode': 200,
        'body': f'File {file_name} saved to {bucket_name}'
    }
