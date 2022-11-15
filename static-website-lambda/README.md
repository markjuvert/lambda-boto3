# Deploy a static website to S3 using Lambda Function

In this demonstration, I deployed a sample static website hosted in S3 using Lambda function. 

The main objective is to automate the whole process so that whenever there is a modification, it can trigger the lambda function to rebuild and deploy the website automatically. 

# The Static Website

The static website is a simple html static template I downloaded from the internet which contains an index.html page and a css and js folders. I have created a github repo and push the static website to. 

## Brief Overview

Create a cloudformation stact which includes the lambda function. When the lambda function is deployed it handlers invoke download the repository from github as a zip file. It then extract the zip file and upload the content of the specified folder to S3.

## 1. Download Content From Github

First, we write a custom lambda function that download the content of the website we want to deply to S3 from Github. We specify the ConstraintDescription (URL), and the specific subdirectory we want to upload to S3.



The logic for downloading respositories from github have the format: account name/archive/main.zip. The files downloaded will be save in /tmp/main.zip. Os.stat gives details of the bytes downloaeded. Extract the files to the target directory and zip.printer will send all the logs to cloudwatch.


## SUMMARY
A CloudFormation is created which invokes lambda custom resources. The lambda function download files from a GitHub repository as a zip file, and extract the file to the lambda execution environment. It then upload only the specific contents to S3 for static website hosting. After the process is complete, it sends a message to CloudFormation as either a success or failure. In addition, a custom domain name was created, configured with cloud front to serve the content.

More details about the project can be found at [static-website](https://cf-lamda.cloud2day.link/).