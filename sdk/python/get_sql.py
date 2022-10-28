from connection import client
from minio.select import (CSVInputSerialization, CSVOutputSerialization,
                          SelectRequest)
                          
with client.select_object_content(
        "myfirstbucket",
        "titanic.csv",
        SelectRequest(
            "select * from S3Object LIMIT 10",
            CSVInputSerialization(),
            CSVOutputSerialization(),
            request_progress=True,
        ),
) as result:
    for data in result.stream():
        print(data.decode())
    print(result.stats())
