# POO y Algoritmos en Python

## Objetivos

- Entender como funciona la POOi

- Entender como medir la eficiencia temporral y espacial de nuestros algoritmos

- Entender como y porque graficar

- Aprender a resolver problemas de busqueda, ordenacion y optimizacion

## Tipos de datos

### Abstractos

En python todo es un objeto y todo tiene un tipo.

- Representacion de datos y formas de interactuar con ellos.

Formas de interactuar con un objeto

- Creacion, manipulacion, destruccioni

Ventajas

- Descomposicion, abstraccion, encapsulacion

Ahora que sabemos que todo en Python es un objeto y es un tipo de dato,

### Instancias

Mientras que la clase es un molde, a los objetos creados se les conoce como instancias

Cuando se crea una instancia, se ejecuta el metodo __init__

Todos los metodos de una clase reciben implicitamente como primer parametro self

Los atributos de clase nos permiten:

- Representar datos

- Procedimientos para interactuar con los mismos metodos

- Mecanismos para esconder la representacion interna

Se accede a los atributos con la notacion de punto

Se pueden tener atributos privados

### Decomposicion

Partir un problema en problemas mas pequenios

Las clases permiten crear mayores abstracciones en forma de componentes

Cada clase se encarga de una parte del problema y el programa se vuelve mas facil de mantener

### Abstraccion

Enfocarnos en la informacion relevante

Separar la informacion central de los detalles secundarios

Podemos utilizar variables y metodos (privados o publicos)

### Encapsulacion

Permite agrupar datos y su comportamiento

Controla el acceso a dichos datos

Previene modificaciones no autorizadas

### Herencia

Permite modelar una jerarquia de clases

Permite compartir comportameinto comun en la jerarquia

Al padre se le conoce como superclase y al huijo como subclase

### Polimorfismo

La habilidad de tomar varias formas

En Python, nos permite cambiar el comportamient de una superclase para adaptarlo a la subclase

## Intro a la complejidad algoritmica

Por que comparamos la eficiencia de un algoritmo

Complejidad temporal vs Complejidad espacial

### Cracion asintotico

No importan variaciones pequenias
