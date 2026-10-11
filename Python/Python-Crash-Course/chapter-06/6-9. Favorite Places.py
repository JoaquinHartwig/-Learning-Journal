# 1. Creamos el diccionario donde los valores son listas
favorite_places = {
    'ariel': ['apóstoles', 'posadas'],
    'joaquín': ['cataratas del iguazú'],
    'valeria': ['bariloche', 'mendoza', 'córdoba'],
}

# 2. Recorremos claves y valores con .items()
for nombre,lugares  in favorite_places.items():
    print(f"\nLos lugares favoritos de {nombre.title()} son:")
    
    # 3. Recorremos la lista de lugares de ESA persona
    for lugar in lugares:
        print(f"\t- {lugar.title()}")