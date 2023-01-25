from connection import client

exist_bucket = client.bucket_exists("dataprev")
if not exist_bucket:
   client.make_bucket("dataprev")
   print("Bucket 'dataprev' criado")
else:
   print("Bucket 'dataprev' já existe")   
   
client.fput_object(
        "dataprev", "INSS/README.txt", "/home/ambientelivre/README.txt",
        content_type="text/plain"
)
print(
    "'home/ambientelivre/README.txt' carregado com sucesso"
    "object 'README.txt' to bucket 'dataprev'."
)

result = client.fput_object(
   "dataprev", "PREVIDENCIA/README.txt", "/home/ambientelivre/README.txt",
    metadata={"ANO_INCLUSAO": "2023"}
)
print(
    "criado objeto {0}; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)
