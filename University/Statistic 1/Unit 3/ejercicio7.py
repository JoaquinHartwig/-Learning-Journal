import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Tasas adaptadas
lambda_a = 2   # 25 horas
lambda_b = 4   # 50 horas
lambda_c = 10  # 125 horas

# Cálculos de probabilidad
prob_a = poisson.pmf(1, mu=lambda_a)
prob_b = poisson.cdf(2, mu=lambda_b)
prob_c = 1 - poisson.cdf(9, mu=lambda_c)

print(f"a) P(X = 1 en 25h)    : {prob_a:.6f} ({prob_a:.2%})")
print(f"b) P(X <= 2 en 50h)   : {prob_b:.6f} ({prob_b:.2%})")
print(f"c) P(X >= 10 en 125h) : {prob_c:.6f} ({prob_c:.2%})")

# Inciso d: Graficar las tres distribuciones
x = np.arange(0, 21)

plt.figure(figsize=(10, 5))
plt.stem(x, poisson.pmf(x, mu=lambda_a), linefmt='r-', markerfmt='ro', basefmt=' ', label='λ = 2 (25h)')
plt.stem(x, poisson.pmf(x, mu=lambda_b), linefmt='g-', markerfmt='go', basefmt=' ', label='λ = 4 (50h)')
plt.stem(x, poisson.pmf(x, mu=lambda_c), linefmt='b-', markerfmt='bo', basefmt=' ', label='λ = 10 (125h)')

plt.title('Distribuciones de Poisson para distintos intervalos de tiempo')
plt.xlabel('Número de componentes fallados (X)')
plt.ylabel('Probabilidad Puntual P(X = x)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()