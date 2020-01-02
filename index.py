import json


def my_handler(input, context):
    return {
        'statucCode': 200,
        'headers': {},
        'body': json.dumps(input)
    }
