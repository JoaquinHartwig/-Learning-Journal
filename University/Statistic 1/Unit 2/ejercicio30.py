# Probabilidades a priori de hacer la tarea
p_r = 0.80
p_no_r = 0.20

# Probabilidades de aprobar según cumplimiento
p_a_dado_r = 0.90
p_a_dado_no_r = 0.60

# Paso 1: Probabilidad Total de aprobar
p_a = (p_r * p_a_dado_r) + (p_no_r * p_a_dado_no_r)

# Paso 2: Teorema de Bayes P(R|A)
p_r_dado_a = (p_r * p_a_dado_r) / p_a

print(f"Probabilidad total de aprobar P(A): {p_a:.4f} ({p_a * 100:.2f}%)")
print(f"Probabilidad P(R|A) con Bayes: {p_r_dado_a:.4f} ({p_r_dado_a * 100:.2f}%)")