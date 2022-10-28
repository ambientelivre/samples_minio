from connection import client

if client.bucket_exists("myfirstbucket"):
    print("myfirstbucket existe")
else:
    print("myfirstbucket não existe")
