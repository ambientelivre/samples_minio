import io
from datetime import datetime, timedelta
from urllib.request import urlopen

from progress import Progress
from connection import client
from minio.commonconfig import GOVERNANCE, Tags
from minio.retention import Retention

# Upload data.
result = client.put_object(
    "pythonbucket", "my-object-simple", io.BytesIO(b"hello"), 5,
)
print(
    "criado objeto {0} ; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)

# Upload do dataset titanic em CSV.
data = urlopen(
    "https://raw.githubusercontent.com/ambientelivre/samples_minio/main/dataset/titanic.csv",
)
result = client.put_object(
    "pythonbucket", "my-object-url-titanic", data, length=-1, part_size=10*1024*1024,
)
print(
    "criado objeto {0} ; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)

# Upload dado setando content-type.
result = client.put_object(
    "pythonbucket", "my-object-content-type", io.BytesIO(b"hello"), 5,
    content_type="application/csv",
)
print(
    "created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)

# Upload dado com metadata.
result = client.put_object(
    "pythonbucket", "my-object-metadata", io.BytesIO(b"hello"), 5,
    metadata={"nomeprojeto": "python-minio"},
)
print(
    "criado objeto {0}; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)

# Upload dado com tags, retention e legal-hold.
# * Deve estar ativa a opção de retenção/locking
date = datetime.utcnow().replace(
    hour=0, minute=0, second=0, microsecond=0,
) + timedelta(days=30)
tags = Tags(for_object=True)
tags["User"] = "ambientelivre"
result = client.put_object(
    "locking", "my-object-retentio", io.BytesIO(b"hello"), 5,
    tags=tags,
    retention=Retention(GOVERNANCE, date),
    legal_hold=True,
)
print(
    "criado objeto {0}; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)

# Upload dados com progress bar visual em Python.
result = client.put_object(
    "pythonbucket", "my-object-progress", io.BytesIO(b"hello"), 5,
    progress=Progress(),
)
print(
    "criado objeto {0}; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    ),
)
