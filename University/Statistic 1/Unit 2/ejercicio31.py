# Probabilidades a priori de producción
p_a = 0.45
p_b = 0.30
p_c = 0.25

# Probabilidades de defecto dado cada máquina
p_d_dado_a = 0.03
p_d_dado_b = 0.04
p_d_dado_c = 0.05

# a) Teorema de la Probabilidad Total
p_d = (p_a * p_d_dado_a) + (p_b * p_d_dado_b) + (p_c * p_d_dado_c)

# b) Teorema de Bayes para B
p_b_dado_d = (p_b * p_d_dado_b) / p_d

# c) Teorema de Bayes para A y C
p_a_dado_d = (p_a * p_d_dado_a) / p_d
p_c_dado_d = (p_c * p_d_dado_c) / p_d

print(f"a) P(Defectuosa): {p_d:.4f} ({p_d*100:.2f}%)")
print(f"b) P(Máquina B | Defectuosa): {p_b_dado_d:.4f} ({p_b_dado_d*100:.2f}%)")
print(f"c) P(Máquina A | Defectuosa): {p_a_dado_d:.4f} ({p_a_dado_d*100:.2f}%)")
print(f"   P(Máquina C | Defectuosa): {p_c_dado_d:.4f} ({p_c_dado_d*100:.2f}%)")