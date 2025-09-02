import os
import boto3
import mimetypes
from botocore.config import Config


def run():
    bucket = os.environ['INPUT_BUCKET']
    region = os.environ['INPUT_REGION']
    folder = os.environ['INPUT_FOLDER']

    configuration = Config(region_name=region)

    s3_client = boto3.client('s3', config=configuration)

    for root, subdirs, files in os.walk(folder):
        for file in files:
            s3_client.upload_file(
                os.path.join(root, file),
                bucket,
                os.path.join(root, file).replace(folder + '/', ''),
                ExtraArgs={"ContentType": mimetypes.guess_type(file)[0]}
            )

    s3_bucket_url = f'http://{bucket}.s3-website-{region}.amazonaws.com'
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f's3-bucket-url={s3_bucket_url}', file=gh_output)


if __name__ == '__main__':
    run()
