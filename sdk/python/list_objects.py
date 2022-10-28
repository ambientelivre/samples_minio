from connection import client

# Lista todos objetos com seus diretórios do bucket
objects = client.list_objects('pythonbucket', prefix='',
                              recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)
