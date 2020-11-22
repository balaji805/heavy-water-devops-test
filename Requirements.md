# Introduction 

This doc describes the solution for the heavy water devops challenge 

https://pasteboard.co/JBzMTJy.png


# Resources Used


Serverless framework has also been used for better management and deployment of the resource

https://www.serverless.com/


AWS SSM PARAMETERS - Contains all the env variables used in the pipeline 

AWS SSM SECRET MANAGER - Used for all the important secrets used in the file

AWS CODEBUILD - Used for creating codebuild steps like deployOnDev, UnitTests , IntegrationTests

Codepipeline - Used for arranging codebuild steps 

Iam Roles - for managing roles for codepipeline and codebuild

Aws Cloudformation - Used for creating cloudformation stacks 


# CodeBuild Steps


https://pasteboard.co/JBzM5fv.png

Source1 -  Used for pulling source code from the github repo using github version 1 and stores it as an artifact whenever a push happens 

UnitTest- This is the frist step that  runs after source build, it unit tests the lambda code to make sure it works 

IntegrationTest  - After unitTest intergtionstep happens which runs integration test with other resources 

Mannual Approval - Once all the steps have passed it needs a manual approval to deploy the code to the production  (optional)

DeployOnProd - Build and deploy the serverless api and bucket to the prod environment 

SelfUpdate- Self updates the pipeline if pipeline code changes 


All the codebuild steps are being observed using a cloudwatch alarm which pushes a message to sns topic hw-codebuild-failed-sns

All the codebuild steps are using the aws/codebuild/amazonlinux2-x86_64-standard:3.0 image which  has python 3.8 preinstalled in it 


# OUTCOMES

1. Master branch will always be live on production
2. Developers can work on branches locally 
3. Once the branch is merged unit tests and integration tests run
4. After which code is deployed to production Using cloudformation  Update hence no downtime might be oversed 
5. If something fails cloudwatch alarm is initiated 

# Serverless Framework Deployment 

All the codePipline is created as code in the codepipeline folder managed by the serverless.yml 

Following serverless plugins have been used 

 - serverless-plugin-existing-s3
  - serverless-dotenv-plugin
  - serverless-offline 
  - serverless-pseudo-parameters


Pipeline can be updated and deployed using the command 

serverless deploy -r << aws.region >>

In the codepipeline folder 


# Future Recommendations

1)  Serverless api and bucket code could also be managed by serverless framework it provides greater flexibility and can also be deployed on other platforms like azure or GCP if required in future 

2) Full github flow for pipeline can be implemented using this flow and if branch names are matined 

https://aws.amazon.com/blogs/devops/implementing-gitflow-using-aws-codepipeline-aws-codecommit-aws-codebuild-and-aws-codedeploy/

3) Iam roles can be tightend using inline policies 

4) One more Dev enviroment should be created on aws for testing and deploying for developer and is more recommended 

# Running CodePipeline on your aws Account 


1. Clone the repo and checkout the master branch 

2. Add the following variables to your ssm folder

```
codebuild_role_arn - Role Arn for codebuild

hw_stack_bucket_name - bucket name for hw bucket 

hw_stack_name - stack name for hw

pipeline_bucket_name - bucket name for storing artifacts



pipeline_githubOwner - github owner name of the repo 


pipeline_githubRepo - github repo name


pipeline_githubBranch - github branch name 
```


3. Add to secrets manager PIPELINE_GITHUB with key githubAccessToken - personal github token key  

4. Go to the codepipeline folder and run serverless deploy -r << aws.region >> if serverless is not installed on your system you can do 
`npm i serverless -g`

That's it Thank You 


