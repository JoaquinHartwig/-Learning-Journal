def formatear_nombre(nombre, apellido, segundo_nombre=""):
    """Devuelve un nombre completo limpio y capitalizado."""
    if segundo_nombre:
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo.title()


cliente_1 = formatear_nombre("juan", "perez")
cliente_2 = formatear_nombre("maria", "gomez", "laura")

print(cliente_1)  # Juan Perez
print(cliente_2)  # Maria Laura Gomez