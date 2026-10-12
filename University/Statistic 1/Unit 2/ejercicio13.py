import math
import itertools

# Total de estudiantes y cargos
m = 8
n = 3


total_asignaciones = math.perm(m, n)

print(f"Total de maneras de asignar los cargos: {total_asignaciones}")


estudiantes = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8']
todas_las_formas = list(itertools.permutations(estudiantes, 3))

print(f"Verificación con itertools: {len(todas_las_formas)} asignaciones")