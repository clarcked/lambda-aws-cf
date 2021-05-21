import os
import urllib.parse


class S3Event:
    def __init__(self, event):
        self.bucket = event['Records'][0]['s3']['bucket']['name']
        self.key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        self.chunks = self.key.split(".")

    def getBucketName(self):
        return self.bucket

    def getKey(self):
        return self.key

    def file(self):
        return self.chunks[0]

    def extension(self):
        return self.chunks[-1]

    def target(self):
        return os.environ['S3_BUCKET_TARGET']

    def destination(self):
        return os.environ["S3_BUCKET_DESTINATION"]
