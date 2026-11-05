flag = True
lista = []

while flag:
    mensage = input("If you could visit one place in the world, where would you go? (Exit para salir): ").strip().lower()
    
    if mensage == 'exit':
        flag = False
    else:
        lista.append(mensage)

print("\nLugares para visitar:")
for listita in lista:
    print(f"- {listita.title()}")