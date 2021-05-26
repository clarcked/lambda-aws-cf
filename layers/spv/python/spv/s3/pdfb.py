import base64
import os

from spv.s3.bucket import Bucket


class PDFBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        self.name = os.environ['S3_BUCKET_PDF']

    def create(self, key, data):
        if not self.has_file(key):
            self.put(key, data)

    def data64(self, key):
        data = self.read(key)
        b64 = base64.b64encode(data)
        return b64.decode("utf-8")
