biblioteca = {
    "LIB01": {
        "titulo": "python crash course",
        "autor": "eric matthes",
        "anio": 2023,
        "prestado": False,
        "categorias": ["Programación", "Data Science"]
    },
    "LIB02": {
        "titulo": "ingeniería de software",
        "autor": "ian sommerville",
        "anio": 2011,
        "prestado": True,
        "categorias": "Ingeniería"
    },
    "LIB03": {
        "titulo": "análisis y diseño de sistemas",
        "autor": "kendall & kendall",
        "anio": 2018,
        "prestado": False,
        "categorias": ["Sistemas", "Análisis"]
    }
}

for clave,diccionario in biblioteca.items():

    titulo = f"{diccionario['titulo']}"
    autor = f"{diccionario['autor']}"
    año = f"{diccionario['anio']}"
    prestado = f"{diccionario['prestado']}"
    categorias = f"{diccionario['categorias']}"
    if diccionario["anio"] >= 2020 and diccionario['prestado'] == False:
        diccionario['prestado']= True
    print()
    print("--------------------------")
    print(f"{clave.title()}")
    print("--------------------------")
 
    print(f"Titulo: {titulo.title()}")
    print(f"Autor: {autor.title()}")
    print(f"Año: {año}")
    if isinstance(diccionario["categorias"],list):
            for categorias in diccionario["categorias"]:
                print(f"Categorias: {categorias.title()}")
    else:
         print(f"Categorias: {categorias.title()}")

    if diccionario["prestado"] == True:
         print("Estado: No disponible prestado")
    else:
         print("Disponible para retiro")
    
    get=diccionario.get('ubicacion',"Ubicacion: Deposito central")
    print(get)