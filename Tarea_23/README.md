# ENUNCIADO DE LA TAREA 23

El alumno debe construir una comunicación cifrada entre dos funciones utilizando el algoritmo del solitario:

1.- Una primera función a la que enviemos una variable (que será una frase o cadena e texto) para que la función lo cifre mediante el solitario. En programación existen diferentes tipos de variables: strings,enteros, flotantes, booleanos, ... y en este caso la variable o parámetro que se le envía a la función es de tipo String.

2.- Una segunda función que recoja el mensaje cifrado y lo descifre utilizando este mismo algoritmo.

# EXPLICACIÓN

Para la solucion de este ejercicio, se ha utilizado una clase Baraja que genera un mazo de cartas y siguiendo los pasos que se dan en la web (http://www.ugr.es/~anillos/textos/pdf/2010/EXPO-1.Criptografia/02a14.htm) se ha resuelto el ejercicio.

En primer lugar, se han creado una clase "Baraja" y una clase "Carta" para generar una baraja real. Partiendo de ahi, se pide al usuario una frase a cifrar y una clave.

En caso de que no se introduzca ninguna clave, se utiliza la baraja creada por defecto tanto para el receptor como para el emisor. En caso de que se introduzca una clave, se convierte cada caracter de la clave a numeros y se realiza el paso 4 del algoritmo del solitario para barajear el mazo siguiendo dicha clave. Con la baraja preparada, se empieza con el cifrado.
Como primer paso del cifrado, se genera una ristra de igual tamaño y disposicion que la frase a cifrar (Cabe destacar que la frase a cifrar se separa en subgrupos de 5 caracteres y que en caso de que falten caracteres se le añaden 'X'-es). Con la ristra generada, se suma la frase a cifrar y la ristra, obteniendo el MENSAJE CIFRADO.

A continuacion, teniendo en cuenta que el emisor y el receptor tienen la misma baraja de la misma manera ordenada, la ristra que generan cada uno de los participantes es la misma, por lo que para descifrar el mensaje, basta con restar la ristra al mensaje cifrado, obteniendo el MENSAJE DESCIFRADO.

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en la ruta theegg_ai/Tarea_23/Tarea_23, donde se pueden encontrar dos archivos con extension ".py". Entre estos, podemos descatar el archivo "Baraja.py" que almacena las clases Baraja y Carta y el archivo "main.py" que almacena la solucion al problema.

En cuanto a la forma de uso, cuando se ejecuta el programa (main.py), este pregunta la frase a cifrar y la clave. En caso de que no se introduzca nada como clave se toma la baraja por defecto tanto para el receptor como para el emisor.
Una vez introducidos los datos mencionados anteriormente (frase y clave) el programa muestra todas las iteracciones de la baraja, la ristra generada, el mensaje cifrado y el mensaje descifrado.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el codigo en linea. Como no manejo el uso de modulos desde esa plataforma, creo las clases Baraja y Carta en el propio main para poder usarla. (https://colab.research.google.com/drive/1rYPoW00TVu49V2w5q1t3LEs4lfiD56cF?usp=sharing)

# POSIBLES MEJORAS

Teniendo en cuenta que este algoritmo esta preparado para descifrar mensajes compuestos por letras del diccionario, en caso de introducir algun caracter que no este en el diccionario (Ñ, Á, É...) el cifrado y descifrado no es completamente correcto. Por eso mismo, reemplazar dichos caracteres por otros de dentro del diccionario seria una opcion. El probema es que estos reemplazamientos tendrian que ser conocidos tanto por el receptor como por el emisor.

Otro aspecto a tener en cuenta, es que en caso de que en la clave (o en la frase) se introduzcan numeros o letras que no pertenezcan al diccionario, el cifrado y descifrado no sera correcto y/o saltara error. Para evitar esto habria que comprobar que las entradas son correctas y en caso contrario, pedir que se vuelvan a introducir.