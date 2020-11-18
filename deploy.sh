
#! /usr/bin/env bash
set -x 
bucket=$1
stack_name=$2
sam package --template-file template.yaml --use-json --s3-bucket ${bucket} --s3-prefix ${stack_name} --output-template-file built_template.json
sam deploy --template-file built_template.json --stack-name ${stack_name} --capabilities CAPABILITY_IAM



