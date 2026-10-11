glosario = {
    "python": "Lenguaje de programación interpretado.",
    "variable": "Espacio en memoria para guardar datos.",
    "bucle": "Estructura que repite un bloque de código."
}
for palabra in glosario.keys():
    print(f"Término: {palabra}")

for palabra in glosario:
    print(palabra)

for palabra in glosario.keys():
    # Usamos la clave 'palabra' para consultar el valor
    significado = glosario[palabra]
    print(f"{palabra.title()}: {significado}")

for palabra in sorted(glosario.keys()):
    print(f"- {palabra}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages.keys():
 print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(f"Hi {name.title()}.")
 if name in friends:
   language = favorite_languages[name].title()
   print(f"\t{name.title()}, I see you love {language}!")