# ENUNCIADOS DE LA TAREA 52

Ejercicios propuestos:

- En el primer ejercicio, desarrolla un programa que sirva para:

	- Solicitar al usuario que ingrese n�meros, los cuales se guardar�n en una lista. Finalizar al ingresar el n�mero 0, el cual no debe guardarse.
	- A continuaci�n, solicitar al usuario que ingrese un n�mero y, si el n�mero est� en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
	- Recorrer la lista para imprimir la sumatoria de todos los elementos.
	- Solicitar al usuario otro n�mero y crear una lista con los elementos de la lista original que sean menores que el n�mero dado. Imprimir esta nueva lista, iterando por ella.
	- Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un n�mero de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendr�: [(5,3), (16,1), (2,2), (57,1)]

- En el segundo ejercicio, solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar 'x'. A continuaci�n, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar 'x'.

	- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.
	- Informar qu� nombres se repiten entre los alumnos de nivel primario y secundario
	- Informar qu� nombres de nivel primario no se repiten en los de nivel secundario.


# EXPLICACI�N

Para la resolucion de ambos ejercicios se deben tener claros los conceptos b�sicos de Python, asi como conocer las estructuras de datos implementables.

En el primer ejercicio, se hace uso de los conocidos Arrays, listas en las que se almacenan diferentes tipos de objetos.

En cuanto al segundo ejercicio, se hace uso de conjuntos, definidos mediante la instruccion 'set()'. Esta estructura se explica a la perfeccion en el primer enlace de las referencias.

# C�DIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

Las soluciones se encuentran en los ficheros "Ejercicio1.py" y "Ejercicio2.py", dentro de la carpeta "tarea_52" y constan de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el c�digo en linea.

- [Enlace Ejercicio 1](https://colab.research.google.com/drive/1oCcorOp03QrpGsQUOJrVkHXbN3zfa7SB?usp=sharing)

- [Enlace Ejercicio 2](https://colab.research.google.com/drive/1G3XICrohE9U20qIrhM13Xu93F2Ta2uow?usp=sharing)


# REFERENCIAS

Cabe destacar, que para la resolucion de este ejercicio se han seguido varias referencias de interes:

	- Conjuntos en Python: https://j2logo.com/python/tutorial/tipo-set-python/
	- Operadores en Python: https://j2logo.com/python/tutorial/operadores-en-python/
	- Ejercicios resueltos de estructuras de datos: http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-estructuras_datos-python.html
	