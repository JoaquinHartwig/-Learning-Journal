# Opciones disponibles por tipo de carácter
letras_disponibles = 26
digitos_disponibles = 10


letras_A = letras_disponibles ** 2
digitos_A = digitos_disponibles ** 4
total_sistema_A = letras_A * digitos_A


letras_B = letras_disponibles ** 3
digitos_B = digitos_disponibles ** 3
total_sistema_B = letras_B * digitos_B


print(f"Sistema A (2L - 4D): {total_sistema_A:,} códigos")
print(f"Sistema B (3L - 3D): {total_sistema_B:,} códigos")