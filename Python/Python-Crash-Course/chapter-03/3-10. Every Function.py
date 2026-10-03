# 1. Crear la lista inicial
paises = ["japón", "canadá", "brasil", "alemania", "australia"]
print(f"Lista inicial: {paises}")

# 2. Acceso por índice y método de string .title()
print(f"Primer país: {paises[0].title()}")
print(f"Último país (índice negativo): {paises[-1].title()}")

# 3. Modificar un elemento
paises[1] = "méxico"
print(f"Después de modificar el índice 1: {paises}")

# 4. Agregar elementos
paises.append("italia")           # Al final
paises.insert(0, "argentina")     # En la posición 0
print(f"Después de append e insert: {paises}")

# 5. Eliminar elementos
del paises[2]                     # Borra el elemento en índice 2
pais_removido = paises.pop()      # Extrae el último
paises.remove("alemania")         # Borra por valor
print(f"Elemento sacado con pop: {pais_removido}")
print(f"Lista tras del, pop y remove: {paises}")

# 6. Longitud de la lista
print(f"Total de países en la lista: {len(paises)}")

# 7. Ordenamiento temporal con sorted()
print(f"Orden temporal (A-Z): {sorted(paises)}")
print(f"Orden temporal (Z-A): {sorted(paises, reverse=True)}")
print(f"Lista sigue intacta: {paises}")

# 8. Invertir orden físico con .reverse()
paises.reverse()
print(f"Lista invertida físicamente: {paises}")

# 9. Ordenamiento permanente con .sort()
paises.sort()
print(f"Orden permanente (A-Z): {paises}")

paises.sort(reverse=True)
print(f"Orden permanente (Z-A): {paises}")