numeros_favoritos = {"ariel":[7,56,424],
                     "santi":[10],
                     "kazy":[69],
                     "facu":[21],
                     "german":[734,71]}

print(numeros_favoritos["ariel"])
print(numeros_favoritos["santi"])
print(numeros_favoritos["kazy"])
print(numeros_favoritos["facu"])
print(numeros_favoritos["german"])

for nombre, numeros_fav in numeros_favoritos.items():
    print(f"Los numeros favoritos de {nombre.title()} son:\t")
    for numeros in numeros_fav:
        print(f"{numeros}")

# Este codigo funciona pq todos los elemos (numeros) son listas, ahora voy a 
#estudiar q pasa si no lo son, y como resolverlos 