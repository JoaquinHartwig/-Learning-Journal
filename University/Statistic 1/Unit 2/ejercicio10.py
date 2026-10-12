letras = 26 #26 pq la ñ no va
numeros = 10 


patentes_anteriores = (letras ** 3) * (numeros ** 3)


patentes_nuevas = (letras ** 4) * (numeros ** 3)

print(f"Sistema Anterior: {patentes_anteriores:,} patentes")
print(f"Sistema Nuevo: {patentes_nuevas:,} patentes")