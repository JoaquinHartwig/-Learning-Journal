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

# Entrada - 10/06/2026

## C# y Programación Orientada a Objetos

Hoy finalicé el curso de C# que estuve siguiendo durante las últimas semanas. Este recorrido me permitió construir una base sólida en los fundamentos del lenguaje y comprender muchos de los conceptos esenciales utilizados en el desarrollo de software moderno.

Más allá de completar el curso, siento que el mayor logro fue desarrollar una comprensión progresiva de la Programación Orientada a Objetos y de la forma en que se estructuran aplicaciones reales.

## Conceptos trabajados

Durante el curso estudié y practiqué temas fundamentales como:

### Fundamentos del lenguaje

* Variables y constantes.
* Conversión de tipos.
* Entrada y salida de datos.
* Operadores aritméticos y lógicos.
* Condicionales (`if`, `else`, `switch`).
* Bucles (`while`, `for`, bucles anidados).
* Métodos y retorno de valores.
* Sobrecarga de métodos.
* Parámetros variables mediante `params`.
* Manejo de excepciones.

### Colecciones y estructuras

* Arrays.
* Arrays multidimensionales.
* Recorridos con `foreach`.
* Listas genéricas (`List<T>`).
* Listas de objetos.

### Programación Orientada a Objetos

* Clases y objetos.
* Constructores.
* Uso de `this`.
* Miembros estáticos.
* Herencia.
* Clases abstractas.
* Polimorfismo.
* Sobrescritura de métodos (`override`).
* Método `ToString()`.
* Interfaces.

### Encapsulamiento y propiedades

* Getters y setters.
* Propiedades autoimplementadas.
* Validación de datos mediante propiedades.
* Diferencia entre campos privados y propiedades públicas.

### Temas avanzados

* Enumeraciones (`enum`).
* Genéricos (`Generics`).
* Introducción al multihilo (`Multithreading`).

## Dificultades encontradas

A medida que avanzaba, algunos de los conceptos más complejos fueron:

* Comprender cuándo utilizar herencia y cuándo utilizar interfaces.
* Entender el verdadero propósito del polimorfismo.
* Diferenciar correctamente entre campos, propiedades y métodos.
* Comprender cómo funcionan internamente los genéricos.
* Visualizar la relación entre clases, objetos y referencias.
* Getters y Setters que diria que es un tema que parece simple,pero no lo es,todavia siento que lo podria reforzar aun más

También descubrí que muchas veces un programa puede funcionar correctamente sin que necesariamente comprenda por completo qué está ocurriendo detrás de escena. Por eso intenté enfocarme en entender la lógica y no solamente en obtener resultados.

## Multihilos

Durante esta etapa únicamente tuve una introducción básica al concepto de multihilo.

Comprendí que permite ejecutar múltiples tareas de manera concurrente dentro de una aplicación, pero considero que todavía es un tema avanzado para mi nivel actual.

Mi objetivo es retomarlo más adelante cuando tenga mayor experiencia desarrollando aplicaciones y pueda apreciar mejor los problemas que intenta resolver.

## Reflexión

Hoy siento que terminé una etapa importante de mi aprendizaje.

Cuando comencé este recorrido, muchos conceptos de C# me resultaban completamente desconocidos. Con el tiempo fui construyendo una base cada vez más sólida mediante práctica, errores, correcciones y ejercicios.

Sin embargo, también comprendí que terminar un curso no significa haber terminado de aprender. En realidad, siento que ahora comienza la parte más interesante: utilizar todos estos conocimientos para construir proyectos propios.

A partir de este momento quiero enfocarme en aplicar lo aprendido mediante programas cada vez más complejos, fortaleciendo mi capacidad para diseñar soluciones, estructurar código y desarrollar software de manera más profesional.

Este curso me dio las herramientas iniciales. Ahora el desafío consiste en transformarlas en experiencia mediante la práctica constante y la creación de proyectos reales.


# Entrada - 11/06/2026

## C# - Turn Based Combat Game (RPG)

La sesión de estudio de hoy fue relativamente corta, pero tuvo un objetivo importante: mantener el hábito de programar y seguir en contacto con el lenguaje, incluso durante una etapa donde gran parte de mi tiempo está dedicada a la universidad y a la preparación de parciales.

No quise repetir el error de meses anteriores, donde dejé completamente de lado C# durante varias semanas y luego tuve que invertir tiempo extra para recuperar fluidez. Por eso decidí dedicar aunque sea un pequeño espacio del día a seguir construyendo proyectos y reforzando conceptos.

### Elección del proyecto

Durante la jornada estuve evaluando distintas ideas de proyectos para continuar practicando programación orientada a objetos. Finalmente decidí comenzar el desarrollo de un pequeño RPG por turnos, un tipo de proyecto que me permite aplicar muchos de los conceptos vistos durante el curso de C#.

El objetivo no es únicamente terminar el juego, sino utilizarlo como una herramienta para consolidar conocimientos y descubrir qué aspectos todavía necesito reforzar.

### Avances realizados

Comencé diseñando una clase `Unit`, que representa una unidad dentro del sistema de combate.

Implementé:

* Atributos privados para almacenar estadísticas.
* Constructor para inicializar cada unidad.
* Sistema básico de ataque.
* Método para recibir daño.
* Generación de daño aleatorio mediante `Random`.

También aproveché el proyecto para comprender mejor cómo interactúan los objetos entre sí, permitiendo que una unidad pueda atacar directamente a otra.

### Conceptos reforzados

Durante esta sesión repasé y utilicé:

* Clases y objetos.
* Constructores.
* Encapsulamiento.
* Métodos.
* Parámetros de tipo objeto.
* Generación de números aleatorios.
* Programación orientada a objetos aplicada a un proyecto real.

### Aspectos a seguir trabajando

Aunque logré avanzar, todavía siento que hay conceptos que necesito incorporar con mayor naturalidad.

Algunas áreas que quiero seguir practicando son:

* Herencia.
* Polimorfismo.
* Interfaces.
* Propiedades.
* Colecciones de objetos.
* Organización de proyectos más grandes.

Mi objetivo es llegar al punto donde estas herramientas formen parte natural de mi forma de programar y no simplemente conceptos aprendidos durante un curso.

### Reflexión

La sesión de hoy confirmó algo que ya venía pensando desde hace tiempo: mantener la constancia es más importante que estudiar muchas horas un solo día.

Aunque el avance fue pequeño, pude seguir en contacto con el lenguaje, trabajar sobre un proyecto que me resulta interesante y mantener vivo el hábito de programar. Considero que esta continuidad será clave para seguir creciendo en C# mientras continúo avanzando con las materias de la universidad.

# C# Daily Log - 13/06/2026

Today I dedicated my free time to C# development and continued working on my Tic-Tac-Toe project.

One interesting discovery was realizing that the tutorial I was following was actually built using WPF, while I had implemented the project as a console application. At first I thought this meant I had taken the wrong approach, but after reflecting on it, I realized that the most important part was understanding and implementing the game logic myself.

During this session I worked on and reinforced several concepts:

* Object-Oriented Programming (OOP)
* Classes and objects
* Properties
* Enums
* Events and delegates
* Two-dimensional arrays
* Turn management
* Win and draw detection logic
* Game state management
* Method analysis and code comprehension

I spent a significant amount of time reading and understanding the code rather than simply copying it. My goal was to understand why each piece exists and how the different classes communicate with one another.

By the end of the session, I managed to get a playable console version of Tic-Tac-Toe running. While there are still improvements to make, the project now has a solid foundation and serves as a practical example of several important C# concepts.

Future improvements include input validation, AI opponents, code refactoring, and eventually rebuilding the project using WPF to learn graphical user interface development.

Today's session reinforced something important: understanding the logic behind the code is far more valuable than simply finishing a project as quickly as possible.

