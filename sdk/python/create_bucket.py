from connection import client

exist_bucket = client.bucket_exists("pythonbucket")
if not exist_bucket:
   client.make_bucket("pythonbucket")
   print("Bucket 'pythonbucket' criado")
else:
   print("Bucket 'pythonbucket' já existe")
