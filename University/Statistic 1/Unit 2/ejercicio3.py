import math
import itertools

n = 5


total_formas = math.factorial(n)

print(f"Cantidad total de secuencias posibles: {total_formas}")




pruebas = ['A', 'B', 'C', 'D', 'E']


todas_las_secuencias = list(itertools.permutations(pruebas))


print(f"Total de formas generadas: {len(todas_las_secuencias)}")
print("\nEjemplo de las primeras 5 secuencias generadas:")
for seq in todas_las_secuencias:
    print(seq)