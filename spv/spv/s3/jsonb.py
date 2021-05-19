from s3 import Bucket
import os


class JSONBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        # self.name = os.getenv['S3_BUCKET_JSON']
        self.name = 'edn-s3-predev-bucket-resumenes-json'

    def load(self, key):
        pass

    def dumps(data):
        pass
