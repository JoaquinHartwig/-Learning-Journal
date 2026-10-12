Ejercicio 1. Listas y manipulación de Strings (Caps. 2 y 3)

    Definí una lista llamada materias que contenga exactamente estos elementos en minúsculas: "english", "estadística 1", "introducción a base de datos 1", "seminario de lenguajes 2".

    Agregá "programación" al final de la lista usando el método de adición correspondiente.

    Insertá "matemáticas" en la primera posición (índice 0).

    Eliminá "english" de la lista usando su valor.

Ejercicio 2. Bucles y F-Strings (Caps. 2 y 4)

    Escribí un bucle for para recorrer la lista materias.

    Dentro del bucle, imprimí un mensaje usando un f-string que diga exactamente: Tengo que preparar el trabajo práctico de [Materia].

    Asegurate de aplicar un método de string para que la primera letra de cada palabra de la materia se imprima en mayúscula (formato título), independientemente de cómo se haya guardado en la lista.

Ejercicio 3. Listas Numéricas y Estadísticas (Cap. 4)

    Creá una lista de números del 1 al 20 inclusive, utilizando la función range().

    Imprimí en tres líneas distintas el número más bajo, el más alto y la suma total de los elementos de esa lista, utilizando las funciones integradas de Python (min, max, sum).

Ejercicio 4. Slicing y Comprehensiones de Listas (Cap. 4)

    Usá una list comprehension (comprensión de lista) en una sola línea de código para generar una lista con los cubos (el número elevado a 3) de los números del 1 al 10.

    Usá slicing para imprimir únicamente los últimos tres resultados de esa lista de cubos.

Ejercicio 5. Tuplas y su inmutabilidad (Cap. 4)

    Definí una tupla llamada horarios_cursada con los elementos "mañana", "tarde", "noche".

    Iterá sobre la tupla con un bucle for e imprimí cada horario.

    Sobrescribí la variable horarios_cursada asignándole una nueva tupla que contenga solo "tarde" y "noche". Volvé a iterar sobre ella e imprimí los nuevos valores para demostrar que la variable original fue reemplazada.

Ejercicio 6 (Nivel Base): Desinfectador y Filtro de Etiquetas (Data Sanitization)

Contexto: En un sistema de base de datos, los usuarios ingresan etiquetas de búsqueda con espacios de más, mezcla de mayúsculas/minúsculas y entradas no permitidas.

Datos de entrada:
Python

raw_tags = ["  python ", "DATABASE ", "  SQL", "django", "  JAVASCRIPT  ", "python", "  ", "C++"]
forbidden_tags = ["c++", "php", "ruby"]

Requerimientos:

    Verificá que raw_tags no esté vacía. Si está vacía, mostrá un mensaje de error y detené la lógica.

    Limpiá cada etiqueta: quitale espacios al inicio/final (.strip()) y convertila a minúsculas (.lower()). Ignorá cualquier entrada que haya quedado totalmente vacía "".

    Creá una nueva lista clean_tags sin duplicados.

    Si la etiqueta limpia está en forbidden_tags, no la agregues a clean_tags y mostrá una advertencia: "Etiqueta bloqueada por política: [etiqueta]".

    Si pasa los filtros, agregala a clean_tags.

    Al final, imprimí la lista resultante clean_tags y cuántas etiquetas válidas quedaron en total.

Ejercicio 7  (Nivel Medio): Análisis de Latencias de Red (Log Diagnostics)

Contexto: Un script de infraestructura recibe métricas de tiempo de respuesta (en milisegundos) de varios servidores. Tenés que procesar los datos para generar un reporte automático.

Datos de entrada:
Python

latencias_ms = [45.2, 120.8, 8.5, 310.0, 95.4, 450.1, 12.0, 88.3]

Requerimientos:

    Validá si la lista contiene métricas.

    Calculá el promedio de latencia (usá sum() y len()) y mostralo redondeado o con formato f-string.

    Obtené las 3 latencias más altas usando rebanados de lista (slices) y ordenamiento, sin destruir el orden original de la lista base.

    Recorré la lista original y clasificá cada latencia:

        Menor a 50.0 ms: "ÓPTIMO"

        Entre 50.0 ms y 150.0 ms (inclusive): "ACEPTABLE"

        Mayor a 150.0 ms: "CRÍTICO - Alerta enviada"

    Imprimí el diagnóstico individual de cada registro y el resumen general (promedio y el top 3 de peores tiempos).

Ejercicio 8 (Nivel Desafío): Matriz de Permisos y Control de Acceso (RBAC Engine)

Contexto: Un sistema Backend debe validar si una solicitud de acceso a un recurso es válida según los permisos que pide el usuario y las reglas del sistema.

Datos de entrada:
Python

permisos_solicitados = ["  READ ", "write", "EXECUTE", "  DELETE  "]
permisos_permitidos_rol = ["read", "write", "execute"]

Requerimientos:

    Normalizá la lista permisos_solicitados (espacios y minúsculas) generando una lista limpia solicitud_normalizada.

    Evaluá las siguientes reglas de negocio mediante condicionales:

        Si el usuario pide "delete" pero no está en permisos_permitidos_rol, rechazá la solicitud entera inmediatamente con el mensaje: "ACCESO DENEGADO: Intento de borrado no autorizado."

        Si la solicitud contiene "write" y "execute", pero NO contiene "read", mostrá una advertencia: "CONFIGURACIÓN INCONSISTENTE: No podés modificar ni ejecutar sin permiso de lectura."

        Filtrá los permisos solicitados contra los permitidos. Generá dos listas: permisos_otorgados y permisos_rechazados.

    Al finalizar, imprimí el reporte final detallando qué permisos se concedieron y cuáles se denegaron.

Ejercicio 9: Flota de vehículos (Lista de diccionarios)

Creá una lista llamada autos que contenga 3 diccionarios. Cada diccionario representa un auto con las claves 'marca', 'modelo', 'año' y 'disponible' (booleano).

    Recorré la lista con un bucle for.

    Si el auto es del año 2020 o posterior, cambiá 'disponible' a True.

    Imprimí únicamente los autos que estén disponibles mostrando la marca, el modelo y el año.

Ejercicio 10: Catálogo de productos (Diccionario de diccionarios)

Creá un diccionario llamado tienda donde cada clave sea el código de un producto (ej. 'P01', 'P02'). El valor de cada clave debe ser un diccionario con 'nombre', 'precio' y 'categoria'.

    Recorré el catálogo imprimiendo el código y los detalles de cada producto con sangría (\t).

    Usá .get() para intentar buscar la clave 'descuento'. Si no existe, la consola debe mostrar "Sin descuento aplicado".

Ejercicio 11: Habilidades de usuarios (Manejo de datos mixtos)

Creá un diccionario llamado usuarios donde las claves sean nombres de desarrolladores. Algunos usuarios tendrán como valor una lista de lenguajes que dominan (ej. ['Python', 'SQL']) y otros tendrán un único lenguaje en un string simple (ej. 'Java').

    Recorré el diccionario con .items().

    Usá isinstance() para detectar si el valor es una lista o un string.

    Si es lista, recorrela con un bucle interno imprimiendo cada lenguaje con un guion (-). Si es un string, imprimilo directamente.

Ejercicio 12 : Proyecto Sistema de Gestión de Biblioteca Técnica

Creá un diccionario llamado biblioteca que contenga el catálogo de libros técnicos de la universidad.

Cada clave del diccionario principal será el código de un libro (ejemplo: "LIB01", "LIB02"). El valor de cada código será otro diccionario con las siguientes propiedades:

    'titulo': String.

    'autor': String.

    'anio': Número entero.

    'prestado': Booleano (True o False).

    'categorias': Puede ser un string simple (si tiene una sola categoría, ej: "Programación") o una lista de strings (si abarca varias, ej: ["Bases de Datos", "Sistemas Operativos"]).

Datos de prueba para tu código:
Python

biblioteca = {
    "LIB01": {
        "titulo": "python crash course",
        "autor": "eric matthes",
        "anio": 2023,
        "prestado": False,
        "categorias": ["Programación", "Data Science"]
    },
    "LIB02": {
        "titulo": "ingeniería de software",
        "autor": "ian sommerville",
        "anio": 2011,
        "prestado": True,
        "categorias": "Ingeniería"
    },
    "LIB03": {
        "titulo": "análisis y diseño de sistemas",
        "autor": "kendall & kendall",
        "anio": 2018,
        "prestado": False,
        "categorias": ["Sistemas", "Análisis"]
    }
}

Lo que tenés que programar:

    Actualización de préstamos:

        Recorré el catálogo. Si el libro fue publicado en 2020 o posterior y actualmente está en False (prestado), cambialo a True (simulando que se reservó automáticamente por ser una edición nueva).

    Reporte por consola:

        Mapeá todos los libros imprimiendo su Código en mayúsculas.

        Mostrá el Título y el Autor aplicando .title().

        Usá .get() para buscar la clave opcional 'ubicacion'. Si la clave no existe en el libro, la consola debe imprimir: "Depósito central".

        Para imprimir las Categorías:

            Usá isinstance() para saber si la propiedad 'categorias' es una lista o un string.

            Si es una lista, recorrela e imprimí cada categoría con un guion (\t- Categoría).

            Si es un string simple, imprimilo directamente con sangría.

        Mostrá el estado final del libro: si prestado es True, imprimí "Estado: No disponible (Prestado)". Si es False, imprimí "Estado: Disponible para retiro".