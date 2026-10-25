# Datos iniciales
universo = 180
m = 85
i = 70
m_inter_i = 50

# a. Solo Matemática
solo_m = m - m_inter_i

# b. Solo Inglés
solo_i = i - m_inter_i

# c. Matemática O Inglés (Unión)
m_union_i = m + i - m_inter_i

# d. Matemática E Inglés (Intersección)
interseccion = m_inter_i

# e. Otras materias
otras = universo - m_union_i

print(f"a) Solo Matemática: {solo_m}")
print(f"b) Solo Inglés: {solo_i}")
print(f"c) Matemática O Inglés: {m_union_i}")
print(f"d) Matemática E Inglés: {interseccion}")
print(f"e) Otras materias: {otras}")