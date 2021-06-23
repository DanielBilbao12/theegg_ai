# ENUNCIADO DE LA TAREA 21
Crea un programa que dado un número entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.

Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número". Debe leer directamente el número que introduzca el usuario. De igual modo, sólo debe mostrar la fracción irreducible encontrada, nada más. Tampoco debe hacer ninguna pausa antes ni después de la ejecución.

# EXPLICACIÓN

Para la solución de este ejercicio, teniendo en cuenta que el valor a introducir por el usuario tiene que ser un numero de 4 cifras decimales como maximo entre 0,0001 y 0,9999, se define 10000 como denominador de manera que el valor introducido (Por ejemplo 0,25) se expresa en forma de fraccion (Siguiendo el ejemplo, 2500/10000). 

Con el valor introducido expresado en modo de fracción, se calcula el maximo comun divisor (MCD) entre ambos numeros (En este caso 2500) y se divide entre el numerador y el denominador (Siguiendo el ejemplo, quedando 1/4)

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "Tarea_21.py" dentro de la carpeta "Tarea_21" y consta de una region en la que se almacena la funcion para el calculo del MCD y el Main, el cual se ejecuta en un bucle infinito en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, el programa simplemente espera a que el usuario introduzca un valor y responde con la fraccion irreducible. En caso de introducir caracteres o nada salta un mensaje de error.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el ejercicio en linea. (https://colab.research.google.com/drive/1sdzHHE3X_-JF-l3J9o3K9wEoJHNH6HgY?usp=sharing)

# POSIBLES MEJORAS

El programa creado se podria mejorar en varios aspectos pero teniendo en cuenta el enunciado y la NOTA del reto, se han seguido dichos criterios.

Como primera mejora, se podria definir mediante una funcion el numero de decimales que va a contener el numero a introducir. En caso de que no se introdujera el numero de decimales dejariamos las 4 cifras decimales como valor constante.
Ademas, se podria comprobar que el valor introducido por el usuario sea un valor decimal con las caracteristicas predefinidas.

Como segunda mejora, en vez de ejecutar el main en un bucle infinito, se podria preguntar al usuario si quiere seguir calculado fracciones irreducibles, en caso de que quiera seguir pues seguiriamos con el proceso de calculo y en caso de que se quiera dejar de calcular la fraccion irreducible detener el programa.
