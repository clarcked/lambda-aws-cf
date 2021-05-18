import boto3


class Bucket:
    def __init__(self) -> None:
        self.client = boto3.client('s3')
        self.name = ""

    def read(self, key):
        pass

    def write(self, key, data):
        pass

    def remove(self, key):
        pass
