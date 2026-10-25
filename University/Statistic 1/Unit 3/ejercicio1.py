from scipy.stats import binom

n = 6
p = 0.55

# a) P(X = 4) - Función de masa de probabilidad (PMF)
p_a = binom.pmf(4, n, p)

# b) P(X = 6)
p_b = binom.pmf(6, n, p)

# c) P(X = 0)
p_c = binom.pmf(0, n, p)

# d) P(2 < X < 4) = P(X = 3)
p_d = binom.pmf(3, n, p)

# e) P(1 <= X <= 4)
# Método 1: Suma de PMFs
p_e_suma = sum(binom.pmf(k, n, p) for k in range(1, 5))

# Método 2: Usando la función de distribución acumulada CDF: P(X <= 4) - P(X <= 0)
p_e_cdf = binom.cdf(4, n, p) - binom.cdf(0, n, p)

print(f"a) P(X=4): {p_a:.4f}")
print(f"b) P(X=6): {p_b:.4f}")
print(f"c) P(X=0): {p_c:.4f}")
print(f"d) P(X=3): {p_d:.4f}")
print(f"e) P(1<=X<=4): {p_e_cdf:.4f}")