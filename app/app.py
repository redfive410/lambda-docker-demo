import sys
import boto3

def handler(event, context):
  client = boto3.client('sts')
  response = client.get_caller_identity()
  return response
