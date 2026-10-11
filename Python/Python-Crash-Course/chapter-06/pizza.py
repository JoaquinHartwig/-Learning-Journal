# El valor de la clave 'ingredientes' es una lista
pizza = {
    'masa': 'gruesa',
    'ingredientes': ['champiñones', 'queso extra', 'albahaca']
}

# Resumen del pedido
print(f"Pediste una pizza de masa {pizza['masa']} con los siguientes ingredientes:")

# Recorremos la lista almacenada en la clave
for ingrediente in pizza['ingredientes']:
    print(f"\t- {ingrediente}")