from scipy.stats import poisson

# Parámetros base
lambda_hora = 18

# Inciso a: P(X <= 24) en 1 hora
prob_a = poisson.cdf(24, mu=lambda_hora)

# Inciso b: P(Y = 3) en 1 minuto (lambda = 18 / 60 = 0.3)
lambda_minuto = 18 / 60
prob_b = poisson.pmf(3, mu=lambda_minuto)

# Impresión de resultados
print(f"a) P(X <= 24 clientes en 1h)   : {prob_a:.6f} ({prob_a:.2%})")
print(f"b) P(Y = 3 clientes en 1 min)  : {prob_b:.6f} ({prob_b:.2%})")