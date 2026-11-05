respuestas = {}
encuesta_activa = True

while encuesta_activa:
    # Captura de datos
    nombre = input("\n¿Cuál es tu nombre? ").strip().title()
    lenguaje = input("¿Qué lenguaje estás aprendiendo? ").strip()
    
    # Asignación clave-valor al diccionario
    respuestas[nombre] = lenguaje
    
    # Pregunta de control para continuar o finalizar el bucle
    repetir = input("¿Quiere responder otra persona? (si/no): ").strip().lower()
    if repetir == 'no':
        encuesta_activa = False

# Mostrar los resultados guardados
print("\n--- Resultados de la encuesta ---")
for nombre, lenguaje in respuestas.items():
    print(f"{nombre} está aprendiendo {lenguaje}.")