# Deploy a static website to S3 using Lambda Function

In this demonstration, I deployed a sample static website hosted in S3 using Lambda function. 

The main objective is to automate the whole process so that whenever there is a modification, it can trigger the lambda function to rebuild and deploy the website automatically. 

# The Static Website

The static website is a simple html static template I downloaded from the internet which contains an index.html page and a css and js folders. I have created a github repo and push the static website to. 

## Brief Overview

Create a cloudformation stact which includes the lambda function. When the lambda function is deployed it handlers invoke download the repository from github as a zip file. It then extract the zip file and upload the content of the specified folder to S3 