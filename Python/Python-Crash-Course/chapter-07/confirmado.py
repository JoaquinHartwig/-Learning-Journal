usuarios_no_confirmados = ['alice', 'brian', 'candace']
usuarios_confirmados = []

# Procesa cada usuario hasta que la lista de origen esté vacía
while usuarios_no_confirmados:
    usuario_actual = usuarios_no_confirmados.pop()
    print(f"Verificando usuario: {usuario_actual.title()}")
    usuarios_confirmados.append(usuario_actual)

print("\nLos siguientes usuarios han sido confirmados:")
for usuario in usuarios_confirmados:
    print(usuario.title())