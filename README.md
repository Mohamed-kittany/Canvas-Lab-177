# AWS Lambda S3 Word Count Exercise

## Lab Overview

In this challenge lab, I developed an AWS Lambda function that activates when a text file is uploaded to an Amazon S3 bucket. The function calculates the word count of the uploaded file and communicates the results via email using Amazon Simple Notification Service (SNS).

## Objectives

The primary goals of this lab included:

- Developing a Lambda function capable of counting words in a text file.
- Configuring an S3 bucket to initiate the Lambda function upon a text file upload.
- Establishing an SNS topic for emailing the word count notification.

## Implementation Steps

1. **S3 Bucket Setup**: I configured an S3 bucket to store uploaded text files.
2. **Lambda Function**: I created a Lambda function in Python to read the file contents, count the words, and relay the results to an SNS topic.
3. **SNS Configuration**: I established an SNS topic and subscribed an email to receive notifications of the word count.

## Challenges and Solutions

Throughout the lab, I encountered several challenges:

### Challenge 1: Import Module Error
**Problem**: I ran into a runtime error stating `[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'lambda_function'`.
**Solution**: I corrected the handler setting in the AWS Lambda console to reflect the actual script name (`S3WordCounterNotifier.lambda_handler`). This adjustment was made in the runtime settings to accurately direct to the handler.

## Monitoring with Amazon CloudWatch

I utilized Amazon CloudWatch to track and log all executions of the function. The CloudWatch logs were crucial for diagnosing problems, notably for pinpointing an incorrect SNS topic ARN and addressing issues related to the Lambda execution role's permissions.

## Technologies Used

- **AWS Lambda**
- **Amazon S3**
- **Amazon SNS**
- **Amazon CloudWatch**

## Conclusion

This lab showcased the capabilities of AWS services in establishing an automated system for processing file uploads and distributing notifications. It also provided valuable hands-on experience in troubleshooting AWS configurations through log analysis and event monitoring.
