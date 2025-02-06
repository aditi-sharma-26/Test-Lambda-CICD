import json


def lambda_handler(event, context):

    print("Hello this is lambda execution.")
    return {
      'statusCode': 200,
      'body': json.dumps('Hello from Lambda! From Github Actions')
    }
