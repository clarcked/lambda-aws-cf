from spv.s3.bucket import Bucket
import os


class JSONBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        self.name = os.environ['S3_BUCKET_JSON']

    def get(self, key):
        return self.read(key).decode("utf-8")
