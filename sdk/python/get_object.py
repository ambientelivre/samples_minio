from minio import Minio
from minio.error import S3Error
from connection import client


# Realiza download de objetos para diretorio local
try:
    client.fget_object('pythonbucket', 'meudiretorio/index.html', 'downloads/index.html')
except S3Error as err:
    print(err)
