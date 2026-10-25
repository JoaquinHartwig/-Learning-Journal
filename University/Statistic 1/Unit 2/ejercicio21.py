# Frecuencias absolutas
N = 180
solo_m = 35
solo_i = 20
m_inter_i = 50
m_total = 85
i_total = 70
m_union_i = 105
otras = 75

# Cálculos de probabilidad
p_a = solo_m / N
p_b = 1 - p_a
p_c = m_union_i / N
p_d = m_inter_i / N
p_e = otras / N
p_f = m_inter_i / m_total  # P(I|M)
p_g = m_inter_i / i_total  # P(M|I)

print(f"a) P(Solo M): {p_a:.4f} ({p_a*100:.2f}%)")
print(f"b) P(NO Solo M): {p_b:.4f} ({p_b*100:.2f}%)")
print(f"c) P(M U I): {p_c:.4f} ({p_c*100:.2f}%)")
print(f"d) P(M n I): {p_d:.4f} ({p_d*100:.2f}%)")
print(f"e) P(Otras): {p_e:.4f} ({p_e*100:.2f}%)")
print(f"f) P(I|M): {p_f:.4f} ({p_f*100:.2f}%)")
print(f"g) P(M|I): {p_g:.4f} ({p_g*100:.2f}%)")