import boto3
from boto3.dynamodb.conditions import Key
import os

class Dynamo:
    def __init__(self, dynamodb=None) -> None:
        if not dynamodb:
            self.dynamodb = boto3.resource('dynamodb')
        self.tableName = os.environ["DYNAMODB_TABLE"]

    def setTableName(self, name):
        self.tableName = name

    def getTable(self):
        return self.dynamodb.Table(self.tableName)

    def query_fecha(self, id_cuenta, fecha):
        response = self.getTable().query(KeyConditionExpression=Key('cuenta_credito').eq(id_cuenta) & Key('aaaamm').eq(fecha))
        return response['Items']

    def query_id(self, id_cuenta):
        response = self.getTable().query(KeyConditionExpression=Key('cuenta_credito').eq(id_cuenta))
        return response['Items']