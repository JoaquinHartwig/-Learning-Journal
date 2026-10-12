import string
import itertools

letras_posibles = 26 ** 3
digitos_posibles = 10 ** 4

total_claves = letras_posibles * digitos_posibles

print(f"Total de contraseñas posibles: {total_claves:,}")

letras = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' (26)
digitos = string.digits           # '0123456789' (10)

# 2. Generamos el total usando la longitud de las variaciones con repetición
bloque_letras = list(itertools.product(letras, repeat=3))
bloque_digitos = list(itertools.product(digitos, repeat=4))

total_simulado = len(bloque_letras) * len(bloque_digitos)

print(f"Variaciones de letras: {len(bloque_letras)}")
print(f"Variaciones de números: {len(bloque_digitos)}")
print(f"Combinaciones totales: {total_simulado}")

# Mostramos un ejemplo de contraseña generada:
ejemplo_letra = "".join(bloque_letras[0])    # 'AAA'
ejemplo_digito = "".join(bloque_digitos[0])   # '0000'
print(f"\nEjemplo de primera contraseña válida: {ejemplo_letra}{ejemplo_digito}")