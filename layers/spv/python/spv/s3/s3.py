import boto3
import json


s3 = boto3.client('s3')


def read_json(key, bucket='edn-s3-predev-bucket-resumenes-json'):
    data = s3.get_object(Bucket=bucket, Key=key)
    dataJson = data['Body'].read().decode("utf-8")
    
    return json.loads(dataJson)

