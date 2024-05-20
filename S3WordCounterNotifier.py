import json
import boto3
import urllib.parse


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-west-2:992382469050:WordCountAlerts'

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    file_obj = s3.get_object(Bucket=bucket, Key=key)
    file_content = file_obj['Body'].read().decode('utf-8')
    word_count = len(file_content.split())

    # Send SNS notification
    sns.publish(
        TopicArn=topic_arn,
        Message=f'The word count in the {key} file is {word_count}.',
        Subject='Word Count Result'
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Word count of {word_count} successfully sent!')
    }
