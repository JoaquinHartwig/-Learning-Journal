raw_tags = ["  python ", "DATABASE ", "  SQL", "django", "  JAVASCRIPT  ", "python", "  ", "C++"]
forbidden_tags = ["c++", "php", "ruby"]


if not raw_tags:
    print("Error: La lista de entrada está vacía.")
else:
    clean_tags = []

    
    for value in raw_tags:
     
        tag_limpia = value.strip().lower()

     
        if tag_limpia == "":
            print("Dato ignorado: Espacios en blanco.")
        
    
        elif tag_limpia in forbidden_tags:
            print(f"Etiqueta bloqueada por política: {tag_limpia}")
        
    
        elif tag_limpia in clean_tags:
            print(f"Etiqueta duplicada ignorada: {tag_limpia}")
        
    
        else:
            clean_tags.append(tag_limpia)

    print("\n--- RESULTADO FINAL ---")
    print(f"Etiquetas válidas: {clean_tags}")
    print(f"Total procesadas con éxito: {len(clean_tags)}")
