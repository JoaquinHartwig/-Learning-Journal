
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