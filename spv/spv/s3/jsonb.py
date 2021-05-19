from spv.s3.bucket import Bucket
import os
import json


class JSONBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        # name = os.environ['S3_BUCKET_JSON']
        # print(name)
        self.name = os.environ['S3_BUCKET_JSON']
        # self.name = 'edn-s3-predev-bucket-resumenes-json'

    def get(self, key):
        return self.read(key).decode("utf-8")

    def dumps(data):
        return json.dumps(data)
