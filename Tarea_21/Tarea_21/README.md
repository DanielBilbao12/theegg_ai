# ENUNCIADO DE LA TAREA 21
Crea un programa que dado un n�mero entre 0,0001 y 0,9999 (y de no m�s de 4 cifras decimales), obtenga y muestre la correspondiente fracci�n irreducible.

Por ejemplo, el n�mero 0,25 se puede obtener a partir de 25/100, o de 2/8, o de 1/4, entre otros. La fracci�n irreducible es 1/4, que est� formada por un numerador y un denominador que son primos entre s�.

Nota: el programa no debe avisar al usuario con mensajes como "Introduzca un n�mero". Debe leer directamente el n�mero que introduzca el usuario. De igual modo, s�lo debe mostrar la fracci�n irreducible encontrada, nada m�s. Tampoco debe hacer ninguna pausa antes ni despu�s de la ejecuci�n.

# EXPLICACION

Para la solucion de este ejercicio, teniendo en cuenta que el valor a introducir por el usuario tiene que ser un numero de 4 cifras decimales como maximo entre 0,0001 y 0,9999, se define 10000 como denominador de manera que el valor introducido (Por ejemplo 0,25) se expresa en forma de fraccion (Siguiendo el ejemplo, 2500/10000). Con el valor introducido expresado en modo de fraccion, se calcula el maximo comun divisor (MCD) entre ambos numeros (En este caso 2500) y se divide entre el numerador y el denominador (Siguiendo el ejemplo, quedando 1/4)
