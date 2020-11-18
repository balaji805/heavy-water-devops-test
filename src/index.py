import boto3
import json
import os
s3 = boto3.resource('s3')
dest_bucket = os.environ['BucketName']


def resize(event, context):
    request_body = json.loads(event['body'])
    obj = s3.Object(
        bucket_name= dest_bucket,
        key= request_body['name'],
    )
    obj.put(Body=json.dumps(request_body['content']), ContentType='application/json')

    
    return {
        "statusCode": 200,
        'body': json.dumps(event),
        'headers': {
            'Content-Type': 'application/json',
        },
    }