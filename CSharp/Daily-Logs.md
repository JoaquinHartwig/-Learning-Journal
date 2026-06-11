# Entrada - 08/06/2026 (semanas anteriores)

## C# y Programación Orientada a Objetos

Durante estos últimos días continué profundizando en el lenguaje C#, avanzando desde conceptos básicos hacia temas más relacionados con la Programación Orientada a Objetos (POO).

### Conceptos trabajados

#### Métodos

Aprendí a crear y utilizar métodos para dividir programas en partes más pequeñas y reutilizables. Practiqué:

* Métodos con parámetros.
* Métodos con valores de retorno mediante `return`.
* Diferencia entre variables locales y parámetros.
* Llamada de métodos desde `Main`.

También comprendí por qué una variable declarada dentro de un método no puede utilizarse directamente desde otro método sin pasarla como argumento.

#### Sobrecarga de métodos

Estudié la sobrecarga de métodos, entendiendo que varios métodos pueden compartir el mismo nombre siempre que tengan firmas diferentes.

Ejemplos trabajados:

* Distinta cantidad de parámetros.
* Distintos tipos de datos.
* Cómo el compilador decide qué versión ejecutar.

#### Palabra clave `params`

Aprendí a utilizar `params` para permitir que un método reciba una cantidad variable de argumentos.

Esto me permitió comprender una forma flexible de diseñar funciones que pueden trabajar con diferentes cantidades de datos de entrada.

### Manejo de excepciones

Comencé a trabajar con:

* `try`
* `catch`
* `finally`

Practicando la captura de errores provocados por:

* Entradas inválidas.
* Conversión incorrecta de datos.
* Operaciones matemáticas problemáticas.

También descubrí que la división entre números de tipo `double` y cero no genera necesariamente una excepción como sucede con enteros, lo que me llevó a investigar el comportamiento interno de los tipos numéricos en C#.

### Arrays multidimensionales

Trabajé con matrices bidimensionales utilizando arreglos como:

```csharp
string[,] estacionamiento
```

Aprendí a:

* Acceder a filas y columnas.
* Recorrer matrices mediante bucles anidados.
* Utilizar `GetLength()` para obtener el tamaño de cada dimensión.

Uno de los conceptos más importantes fue comprender que:

* `GetLength(0)` devuelve la cantidad de filas.
* `GetLength(1)` devuelve la cantidad de columnas.

### Programación Orientada a Objetos

Continué avanzando en conceptos fundamentales de POO:

* Clases.
* Objetos.
* Constructores.
* Herencia.
* Polimorfismo.
* Interfaces.

Además comprendí que en el contexto de la Programación Orientada a Objetos las funciones suelen denominarse métodos porque pertenecen a una clase.

### Git y GitHub

También dediqué tiempo a mejorar la organización de mis repositorios.

Aprendí a:

* Crear y editar archivos README.
* Organizar repositorios de aprendizaje.
* Utilizar GitHub Desktop y Git desde terminal.
* Resolver problemas relacionados con commits, ramas y sincronización con GitHub.

### Reflexión

Durante estos días sentí que empecé a comprender mejor la lógica detrás de C#. Más allá de memorizar sintaxis, intenté enfocarme en entender por qué cada herramienta existe y qué problema intenta resolver.

También avancé en la organización de mi GitHub, transformándolo progresivamente en una documentación pública de mi aprendizaje. Mi objetivo no es únicamente aprender tecnologías, sino registrar de manera consistente el proceso de crecimiento y construcción de habilidades dentro del mundo IT.

# Entrada - 09/06/2026

## C# y Programación Orientada a Objetos

Durante esta jornada retomé el estudio de C# después de haber dedicado varias semanas principalmente a materias de la universidad. Aunque noté que algunos conceptos se habían oxidado por falta de práctica, también descubrí que gran parte de los fundamentos seguían presentes y podían recuperarse rápidamente mediante ejercicios y repaso.

El foco principal estuvo en profundizar conceptos relacionados con Programación Orientada a Objetos (POO), especialmente propiedades, encapsulamiento, polimorfismo e interfaces.

## Conceptos trabajados

### Propiedades (Getters y Setters)

Repasé el uso de propiedades para controlar el acceso a variables privadas dentro de una clase.

Trabajé con ejemplos donde una propiedad valida los datos antes de almacenarlos, evitando estados inválidos para un objeto.

Conceptos reforzados:

* Campos privados.
* Encapsulamiento.
* Propiedades con `get` y `set`.
* Uso de validaciones dentro del setter.
* Diferencia entre modificar directamente un campo privado y utilizar una propiedad.

También comprendí un error frecuente: al asignar valores directamente al campo privado dentro del constructor se evita la ejecución de las validaciones definidas en el setter.

### Constructores y palabra clave `this`

Repasé el propósito de la palabra clave `this`.

Comprendí que permite diferenciar claramente entre:

* Parámetros recibidos por un método o constructor.
* Atributos pertenecientes al objeto actual.

Ejemplo conceptual:

* `nombre` → parámetro.
* `this.nombre` → atributo del objeto.

### Polimorfismo

Comencé a estudiar uno de los pilares más importantes de la Programación Orientada a Objetos.

Analicé el funcionamiento de:

* `virtual`
* `override`

Comprendiendo que:

* `virtual` permite que un método sea redefinido.
* `override` reemplaza la implementación heredada.

También entendí la idea central del polimorfismo:

Una referencia de tipo padre puede almacenar objetos de distintas clases hijas y ejecutar comportamientos diferentes dependiendo del objeto real almacenado.

### Interfaces

Aprendí la diferencia conceptual entre clases e interfaces.

Comprendí que:

* Una clase representa lo que un objeto es.
* Una interfaz representa lo que un objeto puede hacer.

Analicé ejemplos donde diferentes clases implementan una misma interfaz compartiendo capacidades sin necesidad de heredar entre sí.

### Listas de Objetos

Comencé a trabajar con colecciones genéricas utilizando:

```csharp
List<Jugador>
```

Comprendiendo que una lista puede almacenar múltiples objetos creados a partir de una misma clase.

También repasé conceptos relacionados con constructores y creación de instancias dentro de colecciones.

## Dificultades encontradas

La principal dificultad estuvo relacionada con distinguir cuándo una acción se realiza sobre:

* El objeto.
* La propiedad.
* El campo privado interno.

En algunos ejercicios asumía que las validaciones se ejecutaban automáticamente, cuando en realidad estaba modificando directamente los campos internos.

También tuve que reforzar la diferencia entre herencia e interfaces, ya que inicialmente ambos conceptos parecían resolver problemas similares.

## Reflexión

Esta jornada me permitió comprobar algo importante: aunque había dejado temporalmente C# para concentrarme en materias de la carrera, los conocimientos no desaparecieron completamente. Muchos conceptos regresaron con rapidez una vez que volví a practicar.

También confirmé que la programación es una habilidad que requiere contacto frecuente. No necesariamente grandes sesiones de estudio todos los días, pero sí una exposición constante que mantenga frescos los conceptos.

Mi objetivo a partir de ahora es mantener una práctica regular de C#, incluso durante períodos exigentes de la universidad, para evitar largos intervalos sin programar y continuar construyendo una base sólida para proyectos más complejos en el futuro.
