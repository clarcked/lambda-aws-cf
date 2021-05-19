import os
import boto3


class Bucket:
    def __init__(self) -> None:
        self.client = boto3.client('s3')
        self.expiration = os.environ['RESUMEN_EXPIRA']
        self.name = ""

    def sign(self, key):
        params = {'Bucket': self.name, 'Key': key}
        return self.client.generate_presigned_url('get_object', Params=params, ExpiresIn=self.expiration)

    def read(self, key):
        data = self.client.get_object(Bucket=self.name, Key=key)
        return data['Body'].read()

    def write(self, key, data):
        pass

    def remove(self, key):
        pass
