favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for nombre, lenguajes in favorite_languages.items():
    print(f"\nLos lenguajes favoritos de {nombre.title()} son:")
    for lenguaje in lenguajes:
        print(f"\t- {lenguaje.title()}")