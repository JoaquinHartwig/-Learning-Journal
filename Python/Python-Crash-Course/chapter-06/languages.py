favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
#Consulta individual
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Recorrido completo del conjunto

for nombre, lenguaje in favorite_languages.items():
    print(f"El lenguaje favorito de {nombre.title()} es {lenguaje.title()}.")

