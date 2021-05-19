from spv.s3.bucket import Bucket
import os


class PDFBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        self.name = os.environ['S3_BUCKET_PDF']

    def data64(self, key):
        pass
