usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Carlos", "rol": "dev"},
    {"nombre": "Beatriz", "rol": "user"}
]

# Un SOLO bucle for recorre los 3 diccionarios
for usuario in usuarios:
    print(f"Usuario: {usuario['nombre']} | Rol: {usuario['rol']}")