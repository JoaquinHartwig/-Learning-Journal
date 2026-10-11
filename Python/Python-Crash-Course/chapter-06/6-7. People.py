ariel = {"first_name":"Ariel",
         "last_name":"celijoski",
         "age":19,
         "city":"apostoles"}

#print(ariel)

joa = {"first_name":"Joaquin",
       "last_name":"hartwig",
       "age":19,
       "city":"Apostoles"}

valeria = {"first_name":"Valeria",
           "last_name":"lobayan",
           "age":53,
           "city":"Apostoles"}

personas = [ariel,joa,valeria]

for persona in personas:
    nombre_completo = f"{persona['first_name']} {persona['last_name']}".title()
    edad = persona['age']
    ciudad = persona['city'].title()

    print(f"Nombre: {nombre_completo}")
    print(f"Edad: {edad} años")
    print(f"Ciudad: {ciudad}\n")