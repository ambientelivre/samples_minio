from minio import Minio

client = Minio(
    "localhost:9000",
    access_key="ezT3XXVgbUAefg1I",
    secret_key="Ck64zW3nA9ipQoGMTJk8FQRYcNI4AN0W",
    secure=False
)

if client.bucket_exists("myfirstbucket"):
    print("myfirstbucket existe")
else:
    print("myfirstbucket não existe")
