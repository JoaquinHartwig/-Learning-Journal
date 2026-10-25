# Definición de la tabla en un diccionario de frecuencias
total = 1200

hombres = 960
mujeres = 240
ascendidos = 324
no_ascendidos = 876

h_y_a = 288
h_y_na = 672
m_y_a = 36
m_y_na = 204

print(f"d) P(Hombre): {hombres / total:.2f}")
print(f"e) P(Mujer): {mujeres / total:.2f}")
print(f"f) P(Ascendido): {ascendidos / total:.2f}")
print(f"g) P(No ascendido): {no_ascendidos / total:.2f}")
print(f"h) P(Hombre Y Ascendido): {h_y_a / total:.2f}")
print(f"i) P(Hombre Y No ascendido): {h_y_na / total:.2f}")
print(f"j) P(Mujer Y Ascendida): {m_y_a / total:.2f}")
print(f"k) P(Mujer Y No ascendida): {m_y_na / total:.2f}")
print(f"l) P(Hombre O Ascendido): {(hombres + ascendidos - h_y_a) / total:.2f}")
print(f"m) P(Hombre O Mujer): {(hombres + mujeres) / total:.2f}")