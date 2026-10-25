# Generamos el espacio muestral completo
espacio_muestral = [(db, dn) for db in range(1, 7) for dn in range(1, 7)]
total_casos = len(espacio_muestral)  # 36

# a) Suma sea 7
a_fav = [par for par in espacio_muestral if sum(par) == 7]
p_a = len(a_fav) / total_casos

# b) Suma mayor que 9
b_fav = [par for par in espacio_muestral if sum(par) > 9]
p_b = len(b_fav) / total_casos

# c) Suma menor o igual a 7
c_fav = [par for par in espacio_muestral if sum(par) <= 7]
p_c = len(c_fav) / total_casos

# d1) Suma sea 7 u 8
d1_fav = [par for par in espacio_muestral if sum(par) in (7, 8)]
p_d1 = len(d1_fav) / total_casos

# d2) Suma 7 dado que dado blanco = 3
espacio_condicionante = [par for par in espacio_muestral if par[0] == 3]
d2_fav = [par for par in espacio_condicionante if sum(par) == 7]
p_d2 = len(d2_fav) / len(espacio_condicionante)

print(f"a) P(suma = 7): {p_a:.4f} ({p_a*100:.2f}%)")
print(f"b) P(suma > 9): {p_b:.4f} ({p_b*100:.2f}%)")
print(f"c) P(suma <= 7): {p_c:.4f} ({p_c*100:.2f}%)")
print(f"d1) P(suma 7 u 8): {p_d1:.4f} ({p_d1*100:.2f}%)")
print(f"d2) P(suma = 7 | blanco = 3): {p_d2:.4f} ({p_d2*100:.2f}%)")