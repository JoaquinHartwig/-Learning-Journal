rios = {"parana":"argentina",
        "amazonas":"brasil",
        "nilo":"egipto"}

for nombre, pais in rios.items():
    print(f"El {nombre.title()} recorre atravez de {pais.title()}")

for nombre in rios.keys():
    print(f"{nombre.title()}")

for pais in rios.values():
    print(f"{pais.title()}")