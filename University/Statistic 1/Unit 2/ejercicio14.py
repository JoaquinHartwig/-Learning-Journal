import math
import itertools

# Total de personas y tamaño del comité
m = 12
n = 4

# Método A: Cálculo directo con math.comb
total_comites = math.comb(m, n)

print(f"Total de comités posibles: {total_comites}")

# Método B: Verificación generando las combinaciones con itertools
personas = [f"P{i}" for i in range(1, 13)]  # P1, P2, ..., P12
todos_los_comites = list(itertools.combinations(personas, 4))

print(f"Verificación con itertools: {len(todos_los_comites)} comités")