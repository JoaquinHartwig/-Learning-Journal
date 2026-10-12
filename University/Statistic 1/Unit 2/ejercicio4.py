import math
import itertools


mochilas = math.comb(3, 1)    # C(3, 1) = 3
cuadernos = math.comb(6, 3)   # C(6, 3) = 20
boligrafos = math.comb(4, 2)  # C(4, 2) = 6


total_kits = mochilas * cuadernos * boligrafos

print(f"Total de kits escolares posibles: {total_kits}")



# 1. Definimos las opciones de cada artículo
opciones_mochilas = ['Mochila_A', 'Mochila_B', 'Mochila_C']
opciones_cuadernos = list(itertools.combinations(['C1', 'C2', 'C3', 'C4', 'C5', 'C6'], 3))
opciones_bolis = list(itertools.combinations(['Rojo', 'Azul', 'Negro', 'Verde'], 2))

# 2. Generamos el producto cartesiano (todas las combinaciones de los 3 grupos)
todos_los_kits = list(itertools.product(opciones_mochilas, opciones_cuadernos, opciones_bolis))

# 3. Imprimimos el resultado
print(f"Cantidad total de kits generados: {len(todos_los_kits)}")
print("\nEjemplo de los primeros 3 kits de la lista:")
for kit in todos_los_kits[:3]:
    print(kit)