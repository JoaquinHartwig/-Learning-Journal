import math
import itertools


m = 6
n = 3


total_formas = math.perm(m, n) # .perm calulca la permutacion de los valores 
#q le pasamos como parametros

print(f"Total de formas de asignar los analistas: {total_formas}")

analistas = ['Analista_1', 'Analista_2', 'Analista_3', 'Analista_4', 
             'Analista_5', 'Analista_6']
proyectos = ['Proyecto_A', 'Proyecto_B', 'Proyecto_C']

# Generamos las variaciones de 6 elementos tomados de a 3
todas_las_asignaciones = list(itertools.permutations(analistas, 3))

print(f"Cantidad total de asignaciones: {len(todas_las_asignaciones)}")


print("\nPrimeras 3 formas de asignación:")
for asignacion in todas_las_asignaciones[:3]:
    print(dict(zip(proyectos, asignacion)))