toppings = []
message = ""

while message != 'quit':
    message = input("Ingresá un ingrediente ('quit' para terminar): ").strip().lower()
    
    if message != 'quit' and message != "":
        toppings.append(message)
        print(f"-> ¡Agregamos {message} a tu pizza!")

print(f"\nTu pizza incluye: {', '.join(toppings).title()}")