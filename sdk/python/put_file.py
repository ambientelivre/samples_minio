from connection import client

client.fput_object(
        "pythonbucket", "meudiretorio/index.html", "/home/ambientelivre/index.html",
)
print(
    "'home/ambientelivre/index.html' carregado com sucesso"
    "object 'index.html' to bucket 'pythonbucket'."
)
