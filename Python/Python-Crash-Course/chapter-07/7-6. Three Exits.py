#7-4
toppings = []
message = ""

while message != 'quit':
    message = input("Ingresá un ingrediente ('quit' para terminar): ").strip().lower()
    
    if message != 'quit' and message != "":
        toppings.append(message)
        print(f"-> ¡Agregamos {message} a tu pizza!")

print(f"\nTu pizza incluye: {', '.join(toppings).title()}")

#7-5
while True:
    
    entrada = input("Ingresá tu edad ('exit' para salir): ").strip().lower()
    if entrada == 'exit':
        print("¡Gracias por su visita!")
        break
    age = int(entrada)
    if age < 3:
        print("El ticket es gratis ")
    elif age <= 12:
        print("El ticket vale $10")
    else:
        print("El ticket vale $15")
#Test condicional en el encabezado while
entrada = ""

while entrada != 'salir':
    entrada = input("Ingresá tu edad ('salir' para terminar): ").strip().lower()
    
    if entrada != 'salir' and entrada != "":
        edad = int(entrada)
        if edad < 3:
            print("El ticket es gratis")
        elif edad <= 12:
            print("El ticket vale $10")
        else:
            print("El ticket vale $15")

#Variable activa (flag)
activo = True

while activo:
    entrada = input("Ingresá tu edad ('salir' para terminar): ").strip().lower()
    
    if entrada == 'salir':
        activo = False
    elif entrada != "":
        edad = int(entrada)
        if edad < 3:
            print("El ticket es gratis")
        elif edad <= 12:
            print("El ticket vale $10")
        else:
            print("El ticket vale $15")

# Sentencia break
while True:
    entrada = input("Ingresá tu edad ('salir' para terminar): ").strip().lower()
    
    if entrada == 'salir':
        print("¡Gracias por su visita!")
        break
        
    if entrada != "":
        edad = int(entrada)
        if edad < 3:
            print("El ticket es gratis")
        elif edad <= 12:
            print("El ticket vale $10")
        else:
            print("El ticket vale $15")