import random

# Simular lanzar 2 dados y ver la probabilidad de que la suma sea 7 (Ejercicio 24)
ensayos = 100_000
exitos = 0

for _ in range(ensayos):
    dado_blanco = random.randint(1, 6)
    dado_negro = random.randint(1, 6)
    if dado_blanco + dado_negro == 7:
        exitos += 1

probabilidad_simulada = exitos / ensayos
print(f"Probabilidad simulada: {probabilidad_simulada:.4f}") # Cerca de 0.1667 (1/6)