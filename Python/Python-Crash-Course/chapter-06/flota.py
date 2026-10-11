# Generar una flota de 30 aliens automáticamente
flota = []
for s in range(30):
    nuevo_alien = {'color': 'verde', 'puntos': 5, 'velocidad': 'lenta'}
    flota.append(nuevo_alien)

print(f"Total de aliens creados: {len(flota)}")