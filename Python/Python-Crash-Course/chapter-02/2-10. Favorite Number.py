FAVORITE_NUMBER = 7
print(f"My favorite number is {FAVORITE_NUMBER}")

# Para formatear números grandes con separador de miles:
BIG_NUMBER = 1000000
print(f"My balance is ${BIG_NUMBER:,}")  # Imprime: My balance is $1,000,000

# Para rellenar con ceros a la izquierda (por ejemplo, para un código ID):
ID_NUMBER = 7
print(f"User ID: {ID_NUMBER:03d}")        # Imprime: User ID: 007 