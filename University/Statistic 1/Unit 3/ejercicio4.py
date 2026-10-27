from scipy.stats import binom

# Parámetros del problema
n = 10        # Cantidad de insectos
p = 0.20      # Probabilidad de que quede VIVO (1 - 0.80)

# Inciso a: P(X = 2)
prob_a = binom.pmf(k=2, n=n, p=p)

# Inciso b: P(X = 5)
prob_b = binom.pmf(k=5, n=n, p=p)

# Inciso c: Esperanza E(X) = n * p
esperanza = binom.mean(n=n, p=p)

# Resultados
print(f"a) P(X = 2 vivos): {prob_a:.4f} ({prob_a * 100:.2f}%)")
print(f"b) P(X = 5 vivos): {prob_b:.4f} ({prob_b * 100:.2f}%)")
print(f"c) Número esperado de insectos vivos: {esperanza:.1f}")