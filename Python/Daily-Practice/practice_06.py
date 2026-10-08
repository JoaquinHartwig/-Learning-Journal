raw_tags = ["  python ", "DATABASE ", "  SQL", "django", "  JAVASCRIPT  ", "python", "  ", "C++"]
forbidden_tags = ["c++", "php", "ruby"]
if not raw_tags:
    print("Esta vacio la lista")
else:
    print("La lista tiene datos ")

for value in raw_tags:
    if value == " ":
        print("Dato ignorado")
    else:
        value.strip()
        value.lower()
        
for value in raw_tags:
