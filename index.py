import json


def handler(input, context):
    return {
        'statucCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(input)
    }
