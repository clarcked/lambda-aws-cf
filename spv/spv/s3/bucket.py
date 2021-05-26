import os
import boto3
from botocore.exceptions import ClientError


class Bucket:
    def __init__(self) -> None:
        self.client = boto3.client('s3')
        self.expiration = os.environ['RESUMEN_EXPIRA']
        self.name = ""

    def has_file(self, key):
        try:
            obj = self.client.head_object(Bucket=self.name, Key=key)
            return obj["ContentLength"] > 0
        except ClientError as exc:
            print(exc)
            return False

    def sign(self, key):
        params = {'Bucket': self.name, 'Key': key}
        return self.client.generate_presigned_url('get_object', Params=params, ExpiresIn=self.expiration)

    def read(self, key):
        data = self.client.get_object(Bucket=self.name, Key=key)
        return data['Body'].read()

    def put(self, key, data):
        self.client.put_object(Body=data, Bucket=self.name, Key=key)

    def remove(self, key):
        pass
