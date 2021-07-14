# ENUNCIADO DE LA TAREA 48

De una cadena dada de máximo 30 caracteres debéis construir una función que comprima la cadena mediante LZ77 y una función que la descomprima. Evidentemente el input y el output deben coincidir. Los resultados a mostrar al usuario por pantalla son los siguientes:

-Recoger el input de maximo 30 caracteres

-Hacer un print que informe sobre el espacio de memoria que ocupa el string introducido

-Comprimir

-Hacer un print que informe sobre el espacio de memoria que ocupa el string comprimido

-Descomprimir. El Otput debe ser igual que el input

-Hacer un print que informe sobre el espacio de memoria que ocupa el string descomprimido. Una vez descomprimido debera tener el mismo peso que el string original


# EXPLICACIÓN

Para la resolucion del ejercicio se han seguido los siguientes pasos:

En primer lugar, se ha desarrollado una funcion que valide el string introducido por el usuario.

Con la validacion del input realizada, se han desarrollado las funciones encargadas de la compresion/descompresion del string.

Obteniendo el siguiente resultado de ejecucion del programa:

<p align="center">
  <img src="https://raw.githubusercontent.com/DanielBilbao12/theegg_ai/master/tarea_48/ResultadoEjecucion.JPG" alt="Resultado de la ejecucion del programa"/>
</p>

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "tarea_48.py" dentro de la carpeta "tarea_48" y consta de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el código en linea.[Enlace](https://colab.research.google.com/drive/1RNop02PaUhor3nzfHtf-4uUWT2jCQF8P?usp=sharing)


# REFERENCIAS

Cabe destacar, que para la resolucion de este ejercicio se han seguido varias referencias de interes:

	- En el siguiente video se explica de manera gráfica el funcionamiento del algoritmo LZ77: https://www.youtube.com/watch?v=y3xSuPDvpOE
	- En el siguiente enlace se explica el algoritmo mediante un ejemplo: https://timguite.github.io/jekyll/update/2020/03/15/lz77-in-python.html
	- En el siguiente enlace se propone una solucion en python: https://www.programmersought.com/article/86716716490/
	- En el siguiente enlace se explica el algoritmo mediante un ejemplo y se da una solucion en C#: https://www.ecured.cu/Lz77

# POSIBLES MEJORAS

Como posible mejora cabe destacar que no se ha conseguido definir de manera dinamica la longitud de la ventana deslizante ya que en algunas ocasiones, en funcion del input introducido por el usuario y de la longitud definida a la hora de usar la funcion de compresion, el resultado era erroneo.

Para solucionar el error, se ha analizado el funcionamiento del codigo y, en los casos en los que el algoritmo de compresion no finalizada su ejecucion debido al error anteriormente mencionado, se ha forzado la salida del mismo. De esta manera, se consigue la descompresion con una perdida de un caracter respecto al string original. Así, en los casos en los que la descompresion es erronea por la falta de un caracter, se asigna el caracter restante al resultado de la descompresion.
