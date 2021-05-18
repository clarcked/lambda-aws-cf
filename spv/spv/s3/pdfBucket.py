from s3 import Bucket
import os


class PDFBucket(Bucket):
    def __init__(self) -> None:
        super().__init__()
        # self.name = os.environ['S3_BUCKET_PDF']
        self.name = 'edn-s3-predev-bucket-resumenes-json' 

    def data64(self, key):
        pass
