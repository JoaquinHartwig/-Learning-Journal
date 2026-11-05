pedidos_pendientes = ['jamón', 'salame', 'queso']
pedidos_listos = []

# El bucle corre mientras 'pedidos_pendientes' TENGA elementos (sea True)
while pedidos_pendientes:
    # .pop(0) saca el PRIMER elemento y lo guarda en 'sandwich'
    sandwich = pedidos_pendientes.pop(0)
    
    print(f"Preparando: {sandwich}")
    pedidos_listos.append(sandwich)

# Cuando la lista queda vacía ([]), el bucle se detiene
print("\nTodos los pedidos están listos:", pedidos_listos)