import math
import itertools

# Total de libros
n = 5

# Método A: Cálculo directo con factorial
total_ordenamientos = math.factorial(n)

print(f"Total de maneras de ordenar los libros: {total_ordenamientos}")

# Método B: Verificación generando los ordenamientos
libros = ['L1', 'L2', 'L3', 'L4', 'L5']
todas_las_formas = list(itertools.permutations(libros))

print(f"Verificación con itertools: {len(todas_las_formas)} formas")