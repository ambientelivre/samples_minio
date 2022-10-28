from connection import client

buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)
