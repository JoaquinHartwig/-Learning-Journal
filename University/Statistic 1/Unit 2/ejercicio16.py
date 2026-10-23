# Definición de los conjuntos universo y eventos
E = {1, 2, 3, 4, 5, 6}
A = {1, 3, 5}
B = {5, 6}

# i) Operaciones de Conjuntos
A_comp = E - A
A_union_B = A | B
A_union_B_comp = E - A_union_B
B_comp = E - B
A_inter_B = A & B
A_inter_B_comp = E - A_inter_B

# ii) Cálculo de Probabilidades con Regla de Laplace
def prob(conjunto):
    return len(conjunto) / len(E)

print("--- RESULTADOS DE CONJUNTOS Y PROBABILIDADES ---")
print(f"a) A_comp: {A_comp} -> P(A_comp) = {prob(A_comp):.2f}")
print(f"b) A U B: {A_union_B} -> P(A U B) = {prob(A_union_B):.2f}")
print(f"c) (A U B)_comp: {A_union_B_comp} -> P((A U B)_comp) = {prob(A_union_B_comp):.2f}")
print(f"d) B_comp: {B_comp} -> P(B_comp) = {prob(B_comp):.2f}")
print(f"e) A n B: {A_inter_B} -> P(A n B) = {prob(A_inter_B):.2f}")
print(f"f) (A n B)_comp: {A_inter_B_comp} -> P((A n B)_comp) = {prob(A_inter_B_comp):.2f}")