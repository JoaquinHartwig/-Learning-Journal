# Diccionario de usuarios del sistema
users = {
    'aeinstein': {
        'nombre': 'albert',
        'apellido': 'einstein',
        'ubicacion': 'princeton',
    },
    'mcurie': {
        'nombre': 'marie',
        'apellido': 'curie',
        'ubicacion': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    nombre_completo = f"{user_info['nombre']} {user_info['apellido']}"
    ubicacion = user_info['ubicacion']
    
    print(f"\tNombre completo: {nombre_completo.title()}")
    print(f"\tUbicación: {ubicacion.title()}")