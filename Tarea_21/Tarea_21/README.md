# ENUNCIADO DE LA TAREA 21
Crea un programa que dado un número entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales), obtenga y muestre la correspondiente fracción irreducible.

Por ejemplo, el número 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracción irreducible es 1/4, que está formada por un numerador y un denominador que son primos entre sí.

Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un número". Debe leer directamente el número que introduzca el usuario. De igual modo, sólo debe mostrar la fracción irreducible encontrada, nada más. Tampoco debe hacer ninguna pausa antes ni después de la ejecución.

# EXPLICACION

Para la solucion de este ejercicio, teniendo en cuenta que el valor a introducir por el usuario tiene que ser un numero de 4 cifras decimales como maximo entre 0,0001 y 0,9999, se define 10000 como denominador de manera que el valor introducido (Por ejemplo 0,25) se expresa en forma de fraccion (Siguiendo el ejemplo, 2500/10000). Con el valor introducido expresado en modo de fraccion, se calcula el maximo comun divisor (MCD) entre ambos numeros (En este caso 2500) y se divide entre el numerador y el denominador (Siguiendo el ejemplo, quedando 1/4)
