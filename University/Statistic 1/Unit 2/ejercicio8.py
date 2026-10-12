import itertools

digitos = ['1', '3', '5', '7', '9']

# Generamos todas las permutaciones de 3 dígitos (Variación V(5,3))
todas_las_variaciones = list(itertools.permutations(digitos, 3))

# Convertimos las tuplas ('1', '3', '5') a números enteros 135
numeros = [int("".join(p)) for p in todas_las_variaciones]

# a) Total de números
total_a = len(numeros)

# b) Comienzan con 5 (ej: 513)
comienzan_5 = [n for n in numeros if str(n).startswith('5')]

# c) Terminan en 39 (ej: 139)
terminan_39 = [n for n in numeros if str(n).endswith('39')]

# d) Mayores a 600
mayores_600 = [n for n in numeros if n > 600]

print(f"a) Total de números formados: {total_a}")
print(f"b) Números que comienzan con 5: {len(comienzan_5)}")
print(f"c) Números que terminan en 39: {len(terminan_39)} -> {terminan_39}")
print(f"d) Números mayores a 600: {len(mayores_600)}")