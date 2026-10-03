guests = ["Kanye West", "Dionisio", "Socrates"]

print(f"Hola {guests[0].title()}, te invito cordialmente a cenar.")
print(f"Hola {guests[1].title()}, te invito cordialmente a cenar.")
print(f"Hola {guests[2].title()}, te invito cordialmente a cenar.")
print(f"{guests[2].title()}, ¿Por qué no pudiste venir a la cena?")
guests = ["Kanye West", "Dionisio", "Nietzsche"]
print(f"{guests[2].title()}, estas plenamente invitado a mi cena gay")
guests.insert(1,"Illojuan")
guests.insert(2,"Fedro")
guests.insert(3,"Faker")
print(f"Hola {guests[1].title()}, te invito cordialmente a cenar.")
print(f"Hola {guests[2].title()}, te invito cordialmente a cenar.")
print(f"Hola {guests[3].title()}, te invito cordialmente a cenar.")
print(f"Solo invitamos a dos personas a la cena, por motivos especiales estas son: {guests[2].title()} y {guests[4].title()}")
no_invitado = guests.pop(1)
print("Te tuvimos que desenvitar")
no_invitado = guests.pop(5)
print("Te tuvimos que desenvitar")
no_invitado = guests.pop(3)
print("Te tuvimos que desenvitar")
no_invitado = guests.pop(0)


del guests[2]
del guests[4]

print(guests)