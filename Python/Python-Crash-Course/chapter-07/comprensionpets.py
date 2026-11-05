mascotas = ['perro', 'gato', 'perro', 'pez', 'gato', 'conejo', 'gato']

# Reconstruye la lista conservando solo los elementos distintos de 'gato'
mascotas = [mascota for mascota in mascotas if mascota != 'gato']

print(mascotas)
# Salida: ['perro', 'perro', 'pez', 'conejo']