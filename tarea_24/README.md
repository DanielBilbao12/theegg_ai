# ENUNCIADO DE LA TAREA 24

En este caso hay que desarrollar un programa donde una vez enviado un valor decimal a una función este lo convierta a binario y nos lo devuelva. Se trata de construir un simulador de un convertidor analógico digital mediante un programa (software). El hardware lo dejamos para otro día.

# EXPLICACIÓN

Para la solucion de esta tarea, se ha creado una funcion que recibe un numero decimal (entero) y devuelve el valor binario de dicho numero.

Además, se ha creado otra funcion para verificar que el valor introducido por el usuario es un numero entero, en caso contrario, se le vuelve a pedir que introduzca un valor correcto.

# CÓDIGO

El problema se ha resuelto usando Python 3.7 y el IDE Visual Studio 2019.

La solucion se encuentra en el fichero "Tarea_24.py" dentro de la carpeta "Tarea_24" y consta de una region en la que se almacena las funciones y el Main, el cual se ejecuta en un bucle while preguntando si desea realizar otra conversión en cuanto se termina el codigo de la region anteriormente mencionada.

En cuanto a la forma de uso, cuando se ejecuta el programa, se pide al usuario un valor entero y se muestra por pantalla el valor binario de ese numero.

Nota: Dejo el enlace del programa en "Google Colab" para poder ejecutar el código en linea. (https://colab.research.google.com/drive/1pmaUP1vfIUGfvnARfOG7ZUSVTEwN6Wyw?usp=sharing)

# POSIBLES MEJORAS

Como posible mejora, en vez de solo convertir numeros decimales enteros, se podrian convertir los decimales con comas. Cabe destacar, que esta conversion no es del todo exacta ya que la conversion de la parte decimal suele ser una mera aproximacion ya que la conversion de esta parte puede ser infinita.

Como referencia para la conversion de numeros decimales con comas, este video puede ser de ayuda: https://www.youtube.com/watch?v=DG009wcbBw4