favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

nombres = ["jen", "joa " , "      jason", "sarah" , "edward" ,"ariel" , "phil"]

for nombre in nombres:
    nombre = nombre.strip().lower()
    if nombre in favorite_languages:
        print(f"Gracias {nombre.title()} por haber pertenecido a la encuesta")
    else:
        print(f"Porfavor {nombre.title()} haz la encuesta")