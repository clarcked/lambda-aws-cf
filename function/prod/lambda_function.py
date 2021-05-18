
def lambda_handler(event, context):

    # req = event['requestContext']
    # operacion = req['operationName']

    # print(operacion)

    return {
        "statusCode": 200,
        "body": "hello",
        "headers": {
            "Content-Type": "text/html"
        }
    }
