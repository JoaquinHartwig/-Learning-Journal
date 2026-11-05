sandwich_orders = ["jamón y queso", "remolachón", "napolitana", "especial"]
finished_sandwiches = []

# Procesa cada sánguche quitándolo de la lista de entrada y agregándolo a la finalizada
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Extrae el primero de la lista
    print(f"I made your {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nSánguches terminados:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")