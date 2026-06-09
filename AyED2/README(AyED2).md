Entrada - 08/06/2026
Algoritmos y Estructuras de Datos II (AED2)

Durante esta semana profundicé en el estudio de estructuras de datos dinámicas implementadas en lenguaje C, centrándome principalmente en listas enlazadas y pilas.

El objetivo no fue únicamente resolver ejercicios, sino comprender qué ocurre internamente en memoria cuando se crean, recorren, modifican y destruyen estructuras dinámicas mediante punteros.
Conceptos trabajados
Listas enlazadas

    Creación de listas vacías mediante punteros inicializados en NULL.
    Reserva dinámica de memoria utilizando malloc.
    Inserción de elementos al inicio y al final de una lista.
    Eliminación de elementos específicos.
    Recorrido secuencial mediante punteros auxiliares.
    Reconstrucción de listas después de operaciones destructivas.

Pilas

    Implementación utilizando listas enlazadas.

    Operaciones fundamentales:
        apilar
        desapilar
        esVacia

    Comprensión del comportamiento LIFO (Last In, First Out).

    Utilización de estructuras auxiliares para copiar o invertir pilas sin perder información.

Ejercicios realizados

Trabajé con ejercicios de nivel parcial relacionados con:

    Separación de elementos pares e impares.
    Generación de listas de aprobados y desaprobados.
    Cálculo de estadísticas a partir de listas de notas.
    Copia de pilas preservando la estructura original.
    Conversión de listas en pilas.
    Diseño de TDAs para representar entidades más complejas, como alumnos con nombre y nota.

Dificultades encontradas

La mayor dificultad estuvo relacionada con el manejo de punteros y referencias, especialmente al distinguir entre:

    Variables puntero.
    Nodos apuntados por dichos punteros.
    Operadores * y &.
    Punteros a punteros.

También encontré errores frecuentes al trabajar con funciones que modifican directamente estructuras dinámicas, como:

    insertarFinal()
    apilar()
    desapilar()
    sacarElemento()

A medida que avancé, empecé a identificar patrones comunes en la resolución de problemas:

    Las funciones que modifican una estructura suelen requerir acceso directo a ella.
    Las funciones de consulta generalmente trabajan con copias del puntero.
    Comprender el recorrido de referencias es tan importante como comprender el algoritmo en sí.

Reflexión

Hoy sentí un cambio importante en mi forma de abordar estructuras dinámicas. Al comienzo me enfocaba en memorizar funciones y procedimientos, pero durante la práctica descubrí que la verdadera comprensión surge al visualizar constantemente cómo se conectan los nodos y cómo evolucionan los punteros durante la ejecución.

También observé que muchos ejercicios aparentemente distintos comparten una misma estrategia general: recorrer una estructura, procesar información, utilizar estructuras auxiliares cuando es necesario y preservar la integridad de los datos originales.

Aunque todavía cometo errores relacionados con punteros y referencias, terminé la jornada con una comprensión considerablemente más sólida de listas y pilas, dos estructuras fundamentales para temas más avanzados de la materia.
