latencias_ms = [45.2, 120.8, 8.5, 310.0, 95.4, 450.1, 12.0, 88.3]
if not latencias_ms:
    print("La lista no tiene metricas")
else:
    print("La lista tiene metricas")
    suma = sum(latencias_ms)
    total = len(latencias_ms)


promedio = suma/total
print(f"La suma: {suma} y el total es {total} entonces. El promedio es {promedio}")
latencia_ordenada = sorted(latencias_ms)
latencias_altas = latencia_ordenada[-3:] #Devuelve los ultimos 3 elementos sin importar si la lista crece con el paso del tiempo
print(latencias_altas)

for value in latencias_ms:
    if (value < 50.00):
        print(f"Valor Optimo: {value}")
    elif(value <= 150.0):
        print(f"Valor Aceptable: {value}")
    else:
       print(f"Valor Critico: {value}")