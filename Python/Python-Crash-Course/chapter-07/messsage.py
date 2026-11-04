
prompt = "\nEscribí un mensaje y lo repetiré (o escribí 'salir' para terminar): "
message = ""

while message != 'salir':
    message = input(prompt)
    if message != 'salir':
        print(message)