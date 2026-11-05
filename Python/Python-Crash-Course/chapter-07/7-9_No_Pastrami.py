sandwich_orders = [
    "jamón y queso", 
    "remolachón", 
    "pastrami",
    "pastrami", 
    "napolitana", 
    "especial",
    "pastrami"
]
finished_sandwiches = []

# 1. Avisar que no hay stock de pastrami
print("La sanguchería se ha quedado sin pastrami.\n")

# 2. Eliminar todas las ocurrencias de 'pastrami' de la lista de pedidos
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# 3. Procesar los sánguches restantes y moverlos a finished_sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Preparando tu sánguche de {current_sandwich}...")
    finished_sandwiches.append(current_sandwich)

# 4. Mostrar el resumen final
print("\nSánguches terminados:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")