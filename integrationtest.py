import boto3
import botocore
import json

# Set "running_locally" flag if you are running the integration test locally
running_locally = False

if running_locally:

    # Create Lambda SDK client to connect to appropriate Lambda endpoint
    lambda_client = boto3.client('lambda',
        region_name="us-west-1",
        endpoint_url="http://127.0.0.1:3001",
        use_ssl=False,
        verify=False,
        config=botocore.client.Config(
            signature_version=botocore.UNSIGNED,
            read_timeout=1,
            retries={'max_attempts': 0},
        )
    )
else:
    lambda_client = boto3.client('lambda')


response = lambda_client.invoke(FunctionName="heavy-water-demo-ServiceApiFunction-12YSPEQPCTKOW")
# Verify the response
assert response["StatusCode"] == 200
