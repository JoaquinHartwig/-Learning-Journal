# Estructura mixta: Ariel y German tienen listas; Santi, Kazy y Facu tienen enteros simples
numeros_favoritos = {
    "ariel": [7, 56, 424],
    "santi": 10,       # entero simple (no lista)
    "kazy": 69,        # entero simple (no lista)
    "facu": 21,        # entero simple (no lista)
    "german": [734, 71]
}

for nombre, numeros_fav in numeros_favoritos.items():
    # 1. Preguntamos si el valor actual es una lista
    if isinstance(numeros_fav, list):
        print(f"Los números favoritos de {nombre.title()} son:")
        for numero in numeros_fav:
            print(f"\t- {numero}")
    else:
        # 2. Si no es lista, es un dato único y se imprime directamente
        print(f"El número favorito de {nombre.title()} es: {numeros_fav}")
    
    print()  # Línea en blanco para separar