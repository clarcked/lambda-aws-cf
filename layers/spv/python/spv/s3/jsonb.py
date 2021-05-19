import json
import os

from spv.s3.bucket import Bucket


class JSONBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        self.name = os.environ['S3_BUCKET_JSON']

    def get(self, key) -> dict:
        return json.loads(self.read(key).decode("utf-8"))
