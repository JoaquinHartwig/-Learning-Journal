import math

# Total inicial de políticos
politicos = 10

# Paso 1: C(10, 1) para el Presidente
presidente = math.comb(politicos, 1)

# Paso 2: C(9, 2) para los 2 Vicepresidentes
vicepresidentes = math.comb(politicos - 1, 2)

# Paso 3: C(7, 3) para los 3 Vocales
vocales = math.comb(politicos - 1 - 2, 3)

# Aplicamos la Regla del Producto
total_formulas = presidente * vicepresidentes * vocales

print(f"Combinaciones para Presidente: {presidente}")
print(f"Combinaciones para Vicepresidentes: {vicepresidentes}")
print(f"Combinaciones para Vocales: {vocales}")
print(f"\nTotal de fórmulas políticas posibles: {total_formulas:,}")