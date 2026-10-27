from scipy.stats import binom

# Parámetros
n = 19
p = 0.20

# a) A lo sumo 10 zurdos: P(X <= 10)
prob_a = binom.cdf(10, n=n, p=p)

# b) Por lo menos 5 zurdos: P(X >= 5) = 1 - P(X <= 4)
prob_b = 1 - binom.cdf(4, n=n, p=p)

# c) Entre 3 y 6 zurdos: P(3 <= X <= 6) = F(6) - F(2)
prob_c = binom.cdf(6, n=n, p=p) - binom.cdf(2, n=n, p=p)

# d) Esperanza matemática: E(X) = n * p
esperanza = binom.mean(n=n, p=p)

# Impresión formateada sin notación científica
print(f"a) P(X <= 10) : {prob_a:.6f} ({prob_a:.2%})")
print(f"b) P(X >= 5)  : {prob_b:.6f} ({prob_b:.2%})")
print(f"c) P(3<=X<=6) : {prob_c:.6f} ({prob_c:.2%})")
print(f"d) Esperanza E(X): {esperanza:.1f} personas")