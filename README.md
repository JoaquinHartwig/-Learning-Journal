# -Learning-Journal
Diario de aprendizaje 

# 📚 Diario de Aprendizaje
### Joaquin Hartwig — UNaM FCEQyN

---

## Sobre este diario

Registro diario de mi progreso autodidacta
en programación, ciberseguridad e inglés, complementando
mi carrera universitaria.

Creo firmemente que mejorar un 1% cada día
lleva a resultados extraordinarios con el tiempo.

Empecé este diario el 08/06/2026 pero
llevo más de un mes estudiando inglés
y programación de forma diaria antes
de comenzar este registro.

---

## Sobre mí

🎓 Estudiante de Analista en Sistemas /
   Licenciatura en Sistemas de Información
   en la FCEQyN — UNaM, Misiones, Argentina.

💻 Actualmente aprendiendo:
   - C# y Windows Forms
   - Algoritmos y Estructuras de Datos en C
   - Inglés técnico

🎯 Objetivos:
   - Dominar C# y Python
   - Alcanzar nivel C1 en inglés
   - Construir un perfil sólido en IT

---

## Tecnologías que estoy aprendiendo

![C#](https://img.shields.io/badge/C%23-239120?style=flat&logo=csharp)
![C](https://img.shields.io/badge/C-00599C?style=flat&logo=c)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![English](https://img.shields.io/badge/Technical_English-00599C?style=for-the-badge&logo=readthedocs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)

---

## Estructura del diario

Cada entrada diaria incluye:

- **Programación** → ejercicios y conceptos nuevos
- **Inglés** → traducción, vocabulario y comprensión
- **Reflexión** → qué me costó y qué aprendí

---

## Entradas
## Entrada - 08/06/2026

### Inglés Técnico

Hoy continué trabajando con documentación técnica de PostgreSQL y MATLAB. Practiqué la traducción de oraciones complejas relacionadas con programación, bases de datos y procesamiento de datos.

Algunas estructuras que me resultaron difíciles fueron:

* *despite seemingly having protected against it from reaching an aggregate function in the first place*
* *The remaining details of this function definition are not important here so long as they have defaults.*
* *wider scope*
* *These are said to be nested within the outer function.*
* *but to handle each type somewhat differently. MATLAB chooses which M-file to dispatch to based on the type of the input arguments.*

La principal dificultad fue interpretar expresiones completas en lugar de traducir palabra por palabra. En varios casos descubrí que comprender la estructura de la oración era más importante que conocer todas las palabras individualmente.

### Palabras y conceptos aprendidos


* **scope** → ámbito o alcance (Palabra muy utilizada en IT)
* **dispatch** → dirigir o enviar la ejecución a una función específica.
* **defaults** → valores predeterminados. (Tiene otras traducciones,pero esta es la q más me cuesta)
* **remaining** → restante.
* **seemingly** → aparentemente.
* **despite** → a pesar de.
* **handle** → manejar, procesar o tratar.
* **type** → tipo de dato.
* **M-file** → archivo de código MATLAB.
* **wider → más amplio.
* Nuevo vocabulario
seamlessly → de manera fluida, sin interrupciones, sin problemas visibles.
near → cerca de, próximo a.
rough guess → estimación aproximada
enlarges → amplía, agranda, aumenta el tamaño.
wave → onda.

### Reflexión

Hoy confirmé algo que vengo notando desde hace varias semanas: mi comprensión del inglés técnico está mejorando. Hace un tiempo estas oraciones me habrían parecido imposibles de entender, mientras que ahora puedo analizarlas, identificar la estructura gramatical y llegar al significado correcto con ayuda mínima.

También aprendí que muchas palabras técnicas no tienen una traducción literal única y que el contexto es fundamental. Conceptos como *scope*, *dispatch* o *nested* cambian ligeramente según el área de informática en la que se utilicen.

Sigo avanzando de forma gradual. Aunque todavía encuentro oraciones complejas, cada día necesito menos traducción automática y comprendo más contenido directamente en inglés. Mi objetivo sigue siendo alcanzar un nivel que me permita leer documentación técnica y artículos académicos con naturalidad.

# Entrada - 08/06/2026

## Algoritmos y Estructuras de Datos II (AED2)

Esta semana dediqué gran parte del tiempo a trabajar con las estructuras de datos dinámicas vistas en la materia, especialmente listas enlazadas y pilas implementadas en lenguaje C.

Repasé en profundidad el funcionamiento de los punteros dentro de los TDAs, intentando comprender no solo cómo utilizar las funciones sino también qué ocurre en memoria cuando se crean, recorren, modifican o eliminan nodos.

### Conceptos trabajados

**Listas enlazadas**

* Creación de listas vacías mediante punteros inicializados en `NULL`.
* Reserva dinámica de memoria con `malloc`.
* Inserción de elementos al principio y al final de una lista.
* Eliminación de elementos específicos.
* Recorrido de listas utilizando punteros auxiliares.
* Reconstrucción de listas luego de utilizar funciones destructivas como `sacarElemento`.

**Pilas**

* Implementación mediante listas enlazadas.
* Operaciones fundamentales:

  * `apilar`
  * `desapilar`
  * `esVacia`
    
* Comprensión del comportamiento LIFO (Last In, First Out).
* Uso de pilas auxiliares para invertir o copiar estructuras sin perder información.

### Ejercicios realizados

Resolví y analicé varios ejercicios de parcial relacionados con:

* Separación de elementos pares e impares en listas.
* Generación de listas de aprobados y desaprobados.
* Cálculo de porcentajes a partir de listas de notas.
* Copia de pilas conservando los elementos originales.
* Generación de pilas a partir de información almacenada en listas.
* Diseño de TDAs para almacenar estructuras más complejas, como alumnos con nombre y nota.

### Dificultades encontradas

La principal dificultad  comprender con precisión cuándo utilizar:

* `*` (desreferenciación)
* `&` (dirección de memoria)
* Variables de tipo puntero
* Punteros a punteros

Durante varios ejercicios cometí errores al pasar parámetros a funciones del TDA, especialmente en operaciones como:

```
insertarFinal(...)
apilar(...)
desapilar(...)
sacarElemento(...)
```

Sin embargo, a medida que fui resolviendo más ejercicios empecé a identificar un patrón común:

* Si una función debe modificar una lista o pila, generalmente recibe un puntero a la estructura.
* Si una función solamente consulta información, recibe una copia del puntero.
* Cuando se trabaja dentro de la función es necesario distinguir cuidadosamente entre la variable puntero y el nodo al que apunta.

### Reflexión

Hoy sentí que empecé a comprender las estructuras dinámicas de una forma mucho más profunda que en días anteriores. Al principio me enfocaba únicamente en memorizar funciones, pero durante la práctica descubrí que la clave está en visualizar constantemente qué puntero apunta a cada nodo y cómo cambian esas referencias durante la ejecución.

También noté que muchos ejercicios aparentemente distintos comparten la misma lógica general: recorrer una estructura, analizar cada elemento, almacenar resultados en otra estructura auxiliar y finalmente reconstruir la original si fue modificada.

Aunque todavía cometo errores con punteros y referencias, terminé el día con una comprensión mucho más sólida de listas y pilas, dos estructuras fundamentales para los temas más avanzados que veremos en la materia.



