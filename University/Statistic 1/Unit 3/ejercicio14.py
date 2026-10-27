from scipy.stats import binom

# Parámetros
n = 10
p_vivo = 0.20

# a) P(X = 2)
prob_a = binom.pmf(2, n=n, p=p_vivo)

# b) P(X = 5)
prob_b = binom.pmf(5, n=n, p=p_vivo)

# c) Esperanza E(X) = n * p
esperanza = binom.mean(n=n, p=p_vivo)

# Impresión de resultados
print(f"a) P(X = 2 vivos): {prob_a:.6f} ({prob_a:.2%})")
print(f"b) P(X = 5 vivos): {prob_b:.6f} ({prob_b:.2%})")
print(f"c) Número esperado de insectos vivos: {esperanza:.1f}")