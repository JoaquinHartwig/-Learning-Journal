gato = {"mamifero carnivoro":"nuts"}
perro = {"mamifero carnivoro":"mia"}
tortuga = {"reptil":"emilia"}

pets = [gato,perro,tortuga]

for pet in pets:
    for tipo, nombre in pet.items():
        print(f"{tipo.title()}: {nombre.title()}")
      