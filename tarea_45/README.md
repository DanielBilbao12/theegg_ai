# ENUNCIADO DE LA TAREA 45

Se tiene la siguiente lista de elementos:  [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]. Se pide:

-Construir un algoritmo para ordenarlo de menor a mayor

-Buscar el numero 874 mediante el uso de el algoritmo de busqueda secuencial y mediante el algoritmo de busqueda binario. Además, se debe sumar 1 en cada iteracion de modo que al final del programa se indique el numero de iteraciones realizadas por cada algoritmo de busqueda.

-Realizar el analisis en notacion Big-O

# EXPLICACIÓN Y ANALISIS BIG-O

Para la resolucion del ejercicio:

-Se ha aplicado recursividad para crear el algoritmo de ordenacion de menor a mayor.

-En cuanto a la busqueda de forma secuencial y forma binaria, se han seguido los respectivos pasos para cada caso.

Obteniendo el siguiente resultado de ejecucion del programa:

<p align="center">
  <img src="https://raw.githubusercontent.com/DanielBilbao12/theegg_ai/master/tarea_45/ResultadoEjecucion.JPG" alt="Resultado de la ejecucion del programa"/>
</p>

Como se puede observar, el algoritmo de busqueda secuencial necesita mas iteraciones que el algoritmo binario, necesitando mas tiempo para encontrar el numero deseado en la lista.


En cuanto al analisis BIG-O..

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "tarea_45.py" dentro de la carpeta "tarea_45" y consta de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el código en linea.[Enlace](https://colab.research.google.com/drive/1-jvkyllgkC0_gMoBf0rF65c5UcnAwJsl?usp=sharing)

# REFERENCIAS

Cabe destacar, que para la resolucion de este ejercicio se han seguido varias referencias de interes:

	- Enlace sobre el algoritmo de busqueda binaria: https://uniwebsidad.com/libros/algoritmos-python/capitulo-8/busqueda-binaria


# POSIBLES MEJORAS

Como posibles mejoras, se podria pedir al usuario que introduzca una lista para posteriormente ordenarla y, encontrar el numero que el usuario quiera mediante ambos algoritmos de busqueda.
