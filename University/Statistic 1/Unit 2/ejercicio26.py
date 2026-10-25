# Ejercicio 26: Independencia
p_a_26 = 0.3
p_b_26 = 0.4
p_inter_26 = 0.12

p_a_dado_b = p_inter_26 / p_b_26
p_b_dado_a = p_inter_26 / p_a_26
es_independiente = (p_inter_26 == p_a_26 * p_b_26)

print("\n--- EJERCICIO 26 ---")
print(f"a) P(A|B) = {p_a_dado_b:.2f}")
print(f"b) P(B|A) = {p_b_dado_a:.2f}")
print(f"c) ¿Son independientes?: {es_independiente}")