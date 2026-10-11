cities = {
    'apostoles': {
        'country': 'argentina',
        'population': 45_000,
        'fact': 'Es conocida como la Capital Nacional de la Yerba Mate.',
    },
    'tokyo': {
        'country': 'jápón',
        'population': 14_000_000,
        'fact': 'Es el área metropolitana más poblada del mundo.',
    },
    'roma': {
        'country': 'italia',
        'population': 2_800_000,
        'fact': 'Tiene una ciudad-estado independiente en su interior (el Vaticano).',
    },
}

# Recorremos el diccionario exterior (las ciudades)
for city_name, city_info in cities.items():
    print(f"\nCiudad: {city_name.title()}")
    
    # Extraemos los datos del diccionario interior
    pais = city_info['country'].title()
    poblacion = f"{city_info['population']:,}"  # Formateamos el número con comas
    dato = city_info['fact']
    
    print(f"\tPaís: {pais}")
    print(f"\tPoblación aproximada: {poblacion} habitantes")
    print(f"\tDato curioso: {dato}")