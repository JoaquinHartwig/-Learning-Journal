guests = ["Kanye West", "Dionisio", "Socrates"]

# 1. Reemplazamos al que no viene (Socrates en índice 2)
print(f"{guests[2].title()}, ¿Por qué no pudiste venir a la cena?")
guests[2] = "Nietzsche"
print(f"{guests[2].title()}, estás plenamente invitado.")

# 2. Agregamos más invitados (usando insert y append)
guests.insert(0, "Illojuan")
guests.insert(2, "Fedro")
guests.append("Faker")

# La lista actual es: ['Illojuan', 'Kanye West', 'Fedro', 'Dionisio', 'Nietzsche', 'Faker']

print("\n--- REDUCIENDO LA LISTA A SOLO 2 INVITADOS ---")

# Sacamos uno a uno y notificamos
removed = guests.pop() # Saca a Faker
print(f"Lo siento {removed}, no te puedo invitar.")

removed = guests.pop() # Saca a Nietzsche
print(f"Lo siento {removed}, no te puedo invitar.")

removed = guests.pop() # Saca a Dionisio
print(f"Lo siento {removed}, no te puedo invitar.")

removed = guests.pop() # Saca a Fedro
print(f"Lo siento {removed}, no te puedo invitar.")

# Quedan solo 2 personas: Illojuan y Kanye West
print(f"\n{guests[0]} y {guests[1]}, ustedes dos siguen invitados.")

# Vaciamos la lista usando del en los dos únicos elementos que quedan (0 y 0)
del guests[0]
del guests[0]

print(guests) # Muestra: []