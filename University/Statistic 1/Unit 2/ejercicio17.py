# Datos expresados en probabilidades (porcentajes / 100)
p_M = 0.25        # P(Desaprobar Matemática)
p_E = 0.15        # P(Desaprobar Economía)
p_M_inter_E = 0.10 # P(Desaprobar Ambas)

# a) Probabilidad Condicionada: P(M|E) = P(M ∩ E) / P(E)
p_M_dado_E = p_M_inter_E / p_E

# b) Verificación de Independencia: P(M ∩ E) == P(M) * P(E)
son_independientes = (p_M_dado_E == p_M)

# c) Probabilidad de la Unión: P(M U E) = P(M) + P(E) - P(M ∩ E)
p_M_union_E = p_M + p_E - p_M_inter_E

# --- IMPRESIÓN DE RESULTADOS ---
print(f"a) P(Matemática | Economía): {p_M_dado_E:.4f} ({p_M_dado_E * 100:.2f}%)")
print(f"b) ¿Son independientes?: {son_independientes} (P(M|E)={p_M_dado_E:.4f} != P(M)={p_M})")
print(f"c) P(Matemática U Economía): {p_M_union_E:.2f} ({p_M_union_E * 100:.2f}%)")