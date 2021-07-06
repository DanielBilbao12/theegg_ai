# ENUNCIADO DE LA TAREA 44

En esta tarea hay que programar el problema que se plantea en la siguiente secuencia de videos en cualquier lenguaje de programacion:

-[Parte 1](https://www.youtube.com/watch?v=GD254Gotp-4)

-[Parte 2](https://www.youtube.com/watch?v=MaY6FpP0FEU)

# EXPLICACIÓN

Como bien se menciona en el enunciado de la tarea, para la resolucion de este ejercicio se han seguido los pasos indicados en los videos. El objetivo es entender la notacion Big O para analizar la complejidad de los algoritmos.

De esta manera, tras realizar varias pruebas con diferentes rangos de valores a sumar, se concluye que las dos funciones creadas para realizar la suma desde el numero 1 hasta el numro n tienen un coste computacional diferente. A continuacion se muestra el grafico en notacion asintotica que define el nivel de complejidad de ambos algoritmos:

![Comparacion de la complejidad de ambos algoritmos](https://raw.githubusercontent.com/DanielBilbao12/theegg_ai/master/tarea_44/NotacionAsintotica_AmbasFunciones.JPG)

Como se puede apreciar, la funcion que utiliza la formula de Gauss tiene una complejidad constante (mismo numero de operaciones a realizar independientemente del numero de datos de entrada) mientras que la funcion que realiza la suma lineal, aumenta el numero de operaciones a realiza a medida que aumentan el numero de datos de entrada
# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "tarea_44.py" dentro de la carpeta "tarea_44" y consta de una region en la que se almacenan las funciones implementadas y el Main, el cual se ejecuta en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, simplemente hay que ejecutar el programa y visualizar los resultados obtenidos.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el código en linea. [Enlace](https://colab.research.google.com/drive/1VVA9KGFipG_dYxxte30JF7wQTLAi1I3s?usp=sharing)