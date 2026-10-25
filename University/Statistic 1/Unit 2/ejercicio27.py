# Frecuencias absolutas de la tabla
a_y_b = 75       # Inferior a maestría Y menos de 5 años
a_y_no_b = 40    # Inferior a maestría Y 5 o más años
no_a_y_b = 55    # Maestría/superior Y menos de 5 años
no_a_y_no_b = 30 # Maestría/superior Y 5 o más años

total = a_y_b + a_y_no_b + no_a_y_b + no_a_y_no_b # 200
total_a = a_y_b + a_y_no_b                       # 115
total_b = a_y_b + no_a_y_b                       # 130

# Cálculos
p_inter = a_y_b / total
p_union = (total_a + total_b - a_y_b) / total
p_b = total_b / total

# Interpretación 1: Diferencia de conjuntos
p_a_menos_b = a_y_no_b / total
p_b_menos_a = no_a_y_b / total

# Interpretación 2: Probabilidad condicionada
p_a_dado_b = a_y_b / total_b
p_b_dado_a = a_y_b / total_a

print(f"a) P(A n B): {p_inter:.4f} ({p_inter*100:.2f}%)")
print(f"b) P(A U B): {p_union:.4f} ({p_union*100:.2f}%)")
print(f"c) P(B): {p_b:.4f} ({p_b*100:.2f}%)")
print("\n--- Interpretación 1: Diferencia (A - B) ---")
print(f"d) P(A \\ B): {p_a_menos_b:.4f} ({p_a_menos_b*100:.2f}%)")
print(f"e) P(B \\ A): {p_b_menos_a:.4f} ({p_b_menos_a*100:.2f}%)")
print("\n--- Interpretación 2: Condicionada (A | B) ---")
print(f"d) P(A | B): {p_a_dado_b:.4f} ({p_a_dado_b*100:.2f}%)")
print(f"e) P(B | A): {p_b_dado_a:.4f} ({p_b_dado_a*100:.2f}%)")