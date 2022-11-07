import boto3

BUCKET = 'myfirstbucket'
HTTP = 'http://'
ENDPOINT = 'localhost:9000'

FILENAME_ON_S3 = 'storage/background-bi.svg'
PATH_TO_PNG_FILE_ON_DISK = '/home/ambientelivre/Imagens/background-bi.svg'

session = boto3.Session(
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',
    aws_session_token=None,
    botocore_session=None,
    profile_name=None)

s3client = session.client(
    's3', endpoint_url=f"{HTTP}{ENDPOINT}")

s3resource = session.resource(
    's3', endpoint_url=f"{HTTP}{ENDPOINT}")

print('Upload arquivo svg...')
s3resource.Bucket(BUCKET).upload_file(PATH_TO_PNG_FILE_ON_DISK, FILENAME_ON_S3)

print('Upload completo')
